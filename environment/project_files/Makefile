.PHONY: all clean

all: build/app

build/app: src/main.c
	@echo "Compiling application..."
	gcc -o build/app src/main.c
	@echo "Build completed successfully!"

clean:
	rm -f build/app
	@echo "Build artifacts cleaned."
