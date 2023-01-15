default:
	python3 gui.py & 
	python3 file_upload_server.py &
	cd ./server/backend && gin-bin
	cd ../../
	exit
gui:
	python3 gui.py
cli:
	python3 cli.py
website:
	cd backend && go run -tags=jsoniter . && cd ..
