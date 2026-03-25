import os
import subprocess

def converter_biblioteca_inteira(diretorio_base):
    # --- COLOQUE O CAMINHO DO SEU FFMPEG AQUI ---
    ffmpeg_path = r'C:\Users\subzin\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin\ffmpeg.exe'
    
    # Extensões que o script vai procurar para transformar em MP3
    extensoes_para_converter = ('.webm', '.mp4', '.m4a', '.opus')

    print(f"🔍 Vasculhando pastas em: {diretorio_base}")

    convertidos = 0
    erros = 0

    # O os.walk garante que ele entre em todas as pastas de artistas
    for root, dirs, files in os.walk(diretorio_base):
        for file in files:
            if file.lower().endswith(extensoes_para_converter):
                caminho_original = os.path.join(root, file)
                caminho_saida = os.path.splitext(caminho_original)[0] + ".mp3"

                print(f"🎬 Convertendo: {file}")

                comando = [
                    ffmpeg_path,
                    '-i', caminho_original,
                    '-vn', # Remove o vídeo
                    '-ar', '44100',
                    '-ac', '2',
                    '-b:a', '192k',
                    caminho_saida,
                    '-y' # Sobrescreve se já existir um MP3 com o mesmo nome
                ]

                try:
                    # Executa a conversão 
                    subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                    # DELETA o arquivo original (.webm/.mp4) após o sucesso
                    os.remove(caminho_original)
                    convertidos += 1
                except Exception as e:
                    print(f"❌ Erro em {file}: {e}")
                    erros += 1

    print(f"\n✨ FIM DO PROCESSO!")
    print(f"✅ Arquivos convertidos e limpos: {convertidos}")
    print(f"⚠️ Falhas: {erros}")

pasta_alvo = r'C:\Users\subzin\musicas\Minhas_Musicas_MP3'
converter_biblioteca_inteira(pasta_alvo)