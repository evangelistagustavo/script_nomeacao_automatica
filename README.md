# Renomear por Data

Script Python que renomeia arquivos automaticamente, adicionando a data no início do nome.

## Funcionalidade

- Aceita múltiplas pastas, informadas pelo usuário em tempo de execução (Enter vazio encerra a entrada)
- Para cada arquivo, tenta extrair a data em que a foto foi tirada (metadado EXIF)
- Se o arquivo não tiver EXIF (não é imagem, ou não tem essa tag), usa a data de criação do arquivo como alternativa
- Renomeia o arquivo para o formato `AAAA-MM-DD_nomeoriginal.extensão`
- Se uma pasta informada não existir, avisa o usuário e segue para a próxima, sem interromper o processo

## Arquitetura

- `os` para navegação e manipulação de arquivos e pastas
- `datetime` para conversão de timestamp em data legível
- `PIL` (Pillow) para leitura de metadados EXIF de imagens
- Loop externo por pasta, loop interno por arquivo
- `try/except` em duas camadas: uma para pasta inexistente (`FileNotFoundError`), outra para EXIF ausente ou inválido (`UnidentifiedImageError`, `KeyError`), com fallback para a data de criação do arquivo

## Aprendizados

- Diferença entre `os.path.getctime()` (criação) e `os.path.getmtime()` (modificação)
- Leitura de metadados EXIF com Pillow, e a diferença entre `.getexif()` (documentado) e `._getexif()` (não documentado)
- Uso combinado de `try/except` para lidar com múltiplos tipos de erro numa mesma operação
- `continue` para pular iteração de loop sem interromper o processo inteiro
- Formatação de string com `f-string` combinada com raw string (`rf"..."`)

## Limitações conhecidas

- Subpastas dentro da pasta informada também são renomeadas, já que `os.listdir()` não diferencia arquivos de pastas
- A tag EXIF usada (36867, `DateTimeOriginal`) pode não existir em todas as câmeras ou formatos de imagem
- Não há confirmação antes de renomear em massa; recomenda-se testar em pasta de cópia antes de rodar na pasta real

## Próximos passos

- Tratar arquivos que sejam pastas, para não renomeá-los junto com os arquivos
- Explorar outras tags EXIF como alternativa quando `DateTimeOriginal` não existir
