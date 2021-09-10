CC := pip install
FILE := requirements.txt

all:
	while read line; do \
		$(CC) "$$line"; \
		echo "$$line" "has been installed"; \
	done < $(FILE)

	

