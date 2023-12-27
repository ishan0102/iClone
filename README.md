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

## Usage
```bash
python3 main.py
```

## References
Fine-tuning code: https://github.com/ml-explore/mlx-examples/tree/main/lora
