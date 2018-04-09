from bokeh.layouts import row, widgetbox
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.io import output_notebook
from bokeh.palettes import Category20b
from bokeh.layouts import layout

#######################
# X PLOT
#######################

source_x = ColumnDataSource(data=dict(x=x, y=x))


plot_x = figure(
    title='X Joint Probability', 
    x_axis_label="x[i] Displacement (pixels)", 
    y_axis_label="x[i + n] displacement (pixels)", 
    plot_width=400, plot_height=400
)

plot_x.scatter('x', 'y', source=source_x, size=1, color=Category20b[10][3])

callback_x = CustomJS(args=dict(source_x=source_x), code="""
    var data = source_x.data;
    var n = n.value;
    x = data['x']
    y = data['y']
    for (i = 0; i < x.length; i++) {
        y[i + n] = x[i];
    }
    source_x.change.emit();
""")

nx_slider = Slider(start=0, end=10, value=0, step=1,
                    title="n_x", callback=callback_x)
callback_x.args["n"] = nx_slider

#######################
# Y PLOT
#######################
source_y = ColumnDataSource(data=dict(x=y, y=y))

plot_y = figure(
    title='Y Joint Probability', 
    x_axis_label="y[i] displacement (pixels)", 
    y_axis_label="y[i + n] displacement (pixels)", 
    plot_width=400, 
    plot_height=400
)
plot_y.scatter('x', 'y', source=source_y, size=1, color=Category20b[10][6])

callback_y = CustomJS(args=dict(source_y=source_y), code="""
    var data = source_y.data;
    var n = n.value;
    x = data['x']
    y = data['y']
    for (i = 0; i < x.length; i++) {
        y[i + n] = x[i];
    }
    source_y.change.emit();
""")


ny_slider = Slider(start=0, end=10, value=0, step=1,
                    title="n_y", callback=callback_y)
callback_y.args["n"] = ny_slider

layout = layout([[plot_x, plot_y], [widgetbox(nx_slider, ny_slider)]])

output_notebook()

show(layout)
