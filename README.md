# iClone
Clone your friends by finetuning Mistral-7B on your iMessage chat history.
- Built for Apple Silicon MacBooks
- Uses Apple's MLX framework for GPU acceleration
- All data is fetched from and stays on your machine

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

## References
- https://github.com/ml-explore/mlx-examples/tree/main/lora
- https://twitter.com/iamgingertrash/status/1628495957632614400
- https://github.com/1rgs/MeGPT
- https://spin.atomicobject.com/search-imessage-sql
