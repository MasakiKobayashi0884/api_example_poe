# api-example-poe

Python側(FastAPI)でAPIのI/Fを定義してそれをもとにrust-clientでの型情報を自動生成する。

## 環境構築

1. [poetry](https://python-poetry.org/)をインストールしてパスを通す。
2. 仮想環境を構築
```sh
git clone ...
poetry install
```

## rust-client 生成
```sh
poetry run python scripts/generate_client
# -> rust_client/api_example_poe_api
```

## サーバー起動
```sh
poetry run python -m api_example_poe
```

## rust-clientからリクエスト
```sh
cargo run --manifest-path ./rust_client/Cargo.toml
```