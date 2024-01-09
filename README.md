# iClone
Clone your friends by finetuning Mistral-7B on your iMessage chat history.
- Built for Apple Silicon MacBooks
- Uses Apple's MLX framework for GPU acceleration
- All data is fetched from and stays on your machine

## Todo
- Create a basic CLI that lets you choose a chat to finetune on
- Group consecutive messages to create better training data structure
  - Include system prompt, ~5 messages, and prediction of the next message as a single training example
- Trim down the Apple starter code to only what's necessary

## Setup
This copies your iMessage database to the `db` directory to avoid operating on the original file. This file might be kind of big, mine is ~1.5GB.
```bash
cp ~/Library/Messages/chat.db chat.db
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Download Mistral-7B weights:
```bash
curl -o models/mistral-7B.tar https://files.mistral-7b-v0-1.mistral.ai/mistral-7B-v0.1.tar
tar -xf models/mistral-7B.tar
rm models/mistral-7B.tar
```

Convert the model to MLX format:
```bash
python convert.py \
    --torch-model models/mistral-7B/ \
    --mlx-model models/mlx-mistral-7B/
```

Generate some messages:
```bash
python lora.py --model <path_to_model> \
               --adapter-file <path_to_adapters.npz> \
               --num-tokens 50 \
               --prompt "table: 1-10015132-16
columns: Player, No., Nationality, Position, Years in Toronto, School/Club Team
Q: What is terrence ross' nationality
A: "
```

## References
- https://github.com/ml-explore/mlx-examples/tree/main/lora
- https://twitter.com/iamgingertrash/status/1628495957632614400
- https://github.com/1rgs/MeGPT
- https://spin.atomicobject.com/search-imessage-sql
- https://www.izzy.co/blogs/robo-boys.html
- https://edwarddonner.com/2024/01/02/fine-tuning-an-llm-on-240k-text-messages/
- https://github.com/gavi/mlx-whatsapp
