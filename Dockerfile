FROM jupyter/nbviewer

USER root
COPY . /usr/app
RUN cd /usr/app && pip install .

USER nobody
CMD ["python", "-m", "nbviewer", "--port=8080", "--providers=nbviewer_provider",  "--provider_rewrites=nbviewer_provider",  "--frontpage=/usr/app/frontpage.json"]