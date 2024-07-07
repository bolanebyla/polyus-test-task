import uvicorn

from polyus_nsi.adapters.api.app import app

if __name__ == '__main__':
    uvicorn.run(app)
