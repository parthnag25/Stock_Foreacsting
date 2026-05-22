def test_imports():
    import pandas
    import numpy
    import matplotlib
    import yfinance
    import streamlit
    import plotly

    assert pandas.__name__ == 'pandas'
    assert numpy.__name__ == 'numpy'
    assert matplotlib.__name__ == 'matplotlib'
    assert yfinance.__name__ == 'yfinance'
    assert streamlit.__name__ == 'streamlit'
    assert plotly.__name__ == 'plotly'
