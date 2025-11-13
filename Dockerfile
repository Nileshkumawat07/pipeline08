FROM python:3.13.7
COPY ./ web
WORKDIR / web
ENTRYPOINT ["python"]
CMD ["web.py"]
