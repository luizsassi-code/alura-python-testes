#!/bin/bash

echo "Iniciando reset do container MongoDB"

echo "======>>>>> Parando o container atual <<<<<======"
docker compose down -v

echo "======>>>>> Subindo novo container <<<<<======"
docker compose up -d 