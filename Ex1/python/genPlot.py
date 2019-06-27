from bokeh.plotting import figure


def makeHistogram(title, x, y):
    p = figure(title=title, tools='', background_fill_color="#fafafa")
    p.vbar(x=x, top=y, width=80)
    p.line(x, y, line_color="red", line_width=0.8, legend="Comportamento")
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'Tempo'
    p.yaxis.axis_label = 'Valor'
    p.x_range.start = 0
    p.x_range.end = max(x) + 500
    p.y_range.start = min(y)
    p.y_range.end = max(y) + 0.1
    p.grid.grid_line_color = "white"
    return p
