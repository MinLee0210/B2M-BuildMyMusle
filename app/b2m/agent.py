from typing import Union
from transformers import pipeline

class TinyAgent: 
    def __init__(self, config): 
        self.config = config
        self.messages = [
            {"role": "system", 
             "content": "You are a chatbot that specializes in recommending appropriate virtual machine setting for client."}
        ]

    def query(self, 
              query, 
              is_text:bool=True, 
              prettify:bool=True):
        pipe = pipeline(task=self.config['task'], 
                        model=self.config['model_id'])
        
        self.messages.append({"role": "user", 
                              "content": query})
        
        prompt = pipe.tokenizer.apply_chat_template(
            self.messages, tokenize=False, add_generation_prompt=True
        )

        outputs = pipe(prompt,
            **self.config['settings']
        )

        if is_text: 
            outputs = outputs[0]['generated_text']

        if prettify: 
            outputs = self._prettify(outputs)
        return outputs
    
    def _prettify(self, input, special_keyword:str="<|assistant|>"): 
        input = input.split(special_keyword)[-1]
        return input