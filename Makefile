image:
	docker build --rm -t parente/nbviewer-provider .

nbviewer: image
	docker run -it -p 8080:8080 --rm parente/nbviewer-provider