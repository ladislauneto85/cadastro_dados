# Instala as dependências usando pip3
pip3 install -r requirements.txt

# Coleta os arquivos estáticos usando python3
python3 manage.py collectstatic --no-input

# Aplica as migrações do banco de dados usando python3
python3 manage.py migrate