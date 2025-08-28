# RestAPI
API Designed
2h 17m

accepts a notification payload 
if type == warning -> forwarded
if type == info -> ignored

returns all recieved and forwarded notes (stored in mem)


to run :

  req at first:
  pip install -r requirents.txt

  run the server:
  uvicorn main:app --reload

  open swagger ui at http://127.0.0.1:8000/docs

to test:
pytest

