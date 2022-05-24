# Import packages

import yahoo_fin.stock_info as si
import numpy as np
import pandas as pd

aapl_earnings_hist = si.get_earnings_history("aapl")
frame = pd.DataFrame.from_dict(aapl_earnings_hist)
print(frame)

print(si.get_next_earnings_date("aapl"))