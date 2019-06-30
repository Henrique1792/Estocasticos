from bokeh.plotting import figure


def makeHistogram(title, x, xLabel, y, yLabel):
    p = figure(title=title, tools='', background_fill_color="#fafafa")
    p.vbar(x=x, top=y, width=60)
    p.line(x, y, line_color="red", line_width=0.8, legend="Comportamento")
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = xLabel
    p.yaxis.axis_label = yLabel
    p.x_range.start = 0
    p.x_range.end = max(x)
    p.y_range.start = min(y)
    p.y_range.end = max(y)
    p.grid.grid_line_color = "white"
    return p
