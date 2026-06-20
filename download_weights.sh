#!/usr/bin/env bash

echo "====================================="
echo "Baixando pesos do OmniParser v2.0"
echo "====================================="

mkdir -p weights

echo
echo "Baixando detector..."
hf download microsoft/OmniParser-v2.0 icon_detect/model.pt --local-dir weights
hf download microsoft/OmniParser-v2.0 icon_detect/model.yaml --local-dir weights
hf download microsoft/OmniParser-v2.0 icon_detect/train_args.yaml --local-dir weights

echo
echo "Baixando modelo Florence..."
hf download microsoft/OmniParser-v2.0 \
  --include "icon_caption/*" \
  --local-dir weights

echo
echo "====================================="
echo "Download concluido"
echo "====================================="