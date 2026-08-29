FROM ubuntu:latest

# Instalacja pakietów bez czyszczenia cache
RUN apt-get update && apt-get install -y curl openssh-server

# "Sekret" zaszyty w warstwie obrazu
ENV DB_PASSWORD="admin123"

# Otwarty port SSH
EXPOSE 22

# Brak przełączenia na użytkownika nie-root — kontener działa jako root
CMD ["bash"]
