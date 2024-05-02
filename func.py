def salesforecast(month, sales):
    forecast = 0
    month = month.lower()
    if month in ["january", "february", "march"]:
        forecast = sales * 1.1
    elif month in ["april", "may", "june"]:
        forecast = sales * 1.15
    elif month in ["july", "august", "september"]:
        forecast = sales * 1.2
    elif month in ["october", "november", "december"]:
        forecast = sales * 1.25
    return forecast


def sqft(length, width, height):
  sf = 2 * width * height + 2 * length * height + length * width
  return sf
