from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Div(P('Hellow world'), hx_get="/change")

if __name__ == "__main__":
    serve()