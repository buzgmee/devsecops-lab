FROM ubuntu:24.04                         # CKV_DOCKER_7: przypięta wersja

RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*        # czyszczenie cache

# CKV_DOCKER_1: usunięto EXPOSE 22 (bez SSH)
# usunięto ENV DB_PASSWORD — sekret wstrzykujemy w runtime, nie w obrazie

HEALTHCHECK CMD curl --fail http://localhost/ || exit 1   # CKV_DOCKER_2

RUN useradd -m appuser                    # CKV_DOCKER_3: utwórz użytkownika
USER appuser                              # przełącz na nie-root

CMD ["bash"]
