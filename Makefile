dev:
	cd src && python3 main.py

dev-notheme:
	unset GTK_THEME && \
	make dev
