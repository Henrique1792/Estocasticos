from bokeh.plotting import figure


def makeHistogram(title, hist, edges, x, y):
    p = figure(title=title, tools='', background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5)
    p.line(x, y, line_color="red", line_width=0.8, legend="Comportamento")
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'Time'
    p.yaxis.axis_label = 'Value'
    p.grid.grid_line_color = "white"
    return p
