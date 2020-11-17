# [**pyechart教程**](https://github.com/pyecharts/pyecharts-gallery)


## 基本介绍

### 安装pyecharts包
* pip install pyecharts
* pip install pyecharts-jupyter-installer


地图相关的包

* pip install echarts-countries-pypkg  
* pip install echarts-china-provinces-pypkg 
* pip install echarts-china-cities-pypkg 
* pip install echarts-china-counties-pypkg
* pip install echarts-china-misc-pypkg 
* pip install echarts-united-kingdom-pypkg

### 导入包


```python
from pyecharts.globals import CurrentConfig, NotebookType,ThemeType,OnlineHostType
# CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
# CurrentConfig.ONLINE_HOST = "https://assets.pyecharts.org/assets/"
# CurrentConfig.ONLINE_HOST = OnlineHostType.NOTEBOOK_HOST
# CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"

import pyecharts.options as opts
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
```


```python
print(NotebookType.JUPYTER_LAB)
```

    jupyter_lab


### 两种编程方式
* [全局参数设置]( https://pyecharts.org/#/zh-cn/global_options?id=axisopts%ef%bc%9a%e5%9d%90%e6%a0%87%e8%bd%b4%e9%85%8d%e7%bd%ae%e9%a1%b9)

![pyechart](./figs/pyecharts.png)


```python
# 方式一

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.load_javascript()


# 方式二

bar = (
    Bar(
    opts.InitOpts(
    width="900px",
    height="500px",
     renderer= "svg",
    theme= "westeros")
    )
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
)
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
    datazoom_opts=[opts.DataZoomOpts(orient='vertical'),opts.DataZoomOpts(orient='horizontal')],  # vertical   horizontal
    legend_opts = opts.LegendOpts(legend_icon='circle'),
    visualmap_opts= opts.VisualMapOpts(),
    
    toolbox_opts=opts.ToolboxOpts(
        is_show=True,
        orient="vertical",
        pos_left="90%",
        feature=opts.ToolBoxFeatureOpts(
            save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(type_="jpeg", title="保存为jpeg",background_color='white',pixel_ratio=10), # 
            restore=opts.ToolBoxFeatureRestoreOpts(),
            data_view=opts.ToolBoxFeatureDataViewOpts(),
            data_zoom=opts.ToolBoxFeatureDataZoomOpts(),
            magic_type=opts.ToolBoxFeatureMagicTypeOpts(),
            brush=opts.ToolBoxFeatureDataZoomOpts(),
        )
    )
)
bar.load_javascript()
```




    <pyecharts.render.display.Javascript at 0x7ff1b9875d10>




```python
bar.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="9ffa234a64c0457bb2a8894733c0bdfd" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9ffa234a64c0457bb2a8894733c0bdfd = echarts.init(
            document.getElementById('9ffa234a64c0457bb2a8894733c0bdfd'), 'westeros', {renderer: 'svg'});
        var option_9ffa234a64c0457bb2a8894733c0bdfd = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                5,
                20,
                36,
                10,
                75,
                90
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A"
            ],
            "selected": {
                "\u5546\u5bb6A": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14,
            "icon": "circle"
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u886c\u886b",
                "\u7f8a\u6bdb\u886b",
                "\u96ea\u7eba\u886b",
                "\u88e4\u5b50",
                "\u9ad8\u8ddf\u978b",
                "\u889c\u5b50"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "\u4e3b\u6807\u9898",
            "subtext": "\u526f\u6807\u9898",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "itemSize": 15,
        "itemGap": 10,
        "left": "90%",
        "feature": {
            "saveAsImage": {
                "type": "jpeg",
                "backgroundColor": "white",
                "connectedBackgroundColor": "#fff",
                "show": true,
                "title": "\u4fdd\u5b58\u4e3ajpeg",
                "pixelRatio": 10
            },
            "restore": {
                "show": true,
                "title": "\u8fd8\u539f"
            },
            "dataView": {
                "show": true,
                "title": "\u6570\u636e\u89c6\u56fe",
                "readOnly": false,
                "lang": [
                    "\u6570\u636e\u89c6\u56fe",
                    "\u5173\u95ed",
                    "\u5237\u65b0"
                ],
                "backgroundColor": "#fff",
                "textareaColor": "#fff",
                "textareaBorderColor": "#333",
                "textColor": "#000",
                "buttonColor": "#c23531",
                "buttonTextColor": "#fff"
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "\u533a\u57df\u7f29\u653e",
                    "back": "\u533a\u57df\u7f29\u653e\u8fd8\u539f"
                },
                "icon": {},
                "xAxisIndex": false,
                "yAxisIndex": false,
                "filterMode": "filter"
            },
            "magicType": {
                "show": true,
                "type": [
                    "line",
                    "bar",
                    "stack",
                    "tiled"
                ],
                "title": {
                    "line": "\u5207\u6362\u4e3a\u6298\u7ebf\u56fe",
                    "bar": "\u5207\u6362\u4e3a\u67f1\u72b6\u56fe",
                    "stack": "\u5207\u6362\u4e3a\u5806\u53e0",
                    "tiled": "\u5207\u6362\u4e3a\u5e73\u94fa"
                },
                "icon": {}
            },
            "brush": {
                "show": true,
                "title": {
                    "zoom": "\u533a\u57df\u7f29\u653e",
                    "back": "\u533a\u57df\u7f29\u653e\u8fd8\u539f"
                },
                "icon": {},
                "xAxisIndex": false,
                "yAxisIndex": false,
                "filterMode": "filter"
            }
        }
    },
    "visualMap": {
        "show": true,
        "type": "continuous",
        "min": 0,
        "max": 100,
        "inRange": {
            "color": [
                "#50a3ba",
                "#eac763",
                "#d94e5d"
            ]
        },
        "calculable": true,
        "inverse": false,
        "splitNumber": 5,
        "orient": "vertical",
        "showLabel": true,
        "itemWidth": 20,
        "itemHeight": 140,
        "borderWidth": 0
    },
    "dataZoom": [
        {
            "show": true,
            "type": "slider",
            "realtime": true,
            "start": 20,
            "end": 80,
            "orient": "vertical",
            "zoomLock": false,
            "filterMode": "filter"
        },
        {
            "show": true,
            "type": "slider",
            "realtime": true,
            "start": 20,
            "end": 80,
            "orient": "horizontal",
            "zoomLock": false,
            "filterMode": "filter"
        }
    ]
};
        chart_9ffa234a64c0457bb2a8894733c0bdfd.setOption(option_9ffa234a64c0457bb2a8894733c0bdfd);
    </script>
</body>
</html>




## bar可视化


```python
c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
)
c.set_global_opts(
    title_opts=opts.TitleOpts(title="主标题", title_link=None, subtitle="副标题",subtitle_link=None),
    toolbox_opts=opts.ToolboxOpts(
        is_show=True,
        orient="vertical",
        feature=opts.ToolBoxFeatureOpts(
            save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(type_="jpeg", title="保存为jpeg",background_color='white',pixel_ratio=10), # 
            restore=opts.ToolBoxFeatureRestoreOpts(),
            data_view=opts.ToolBoxFeatureDataViewOpts(),
            data_zoom=opts.ToolBoxFeatureDataZoomOpts(),  # 'horizontal', 'vertical'
            magic_type=opts.ToolBoxFeatureMagicTypeOpts(),
            brush=opts.ToolBoxFeatureBrushOpts(),
        )
    )
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="9834d3405aae447da47ed60d5c3d4d30" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9834d3405aae447da47ed60d5c3d4d30 = echarts.init(
            document.getElementById('9834d3405aae447da47ed60d5c3d4d30'), 'white', {renderer: 'canvas'});
        var option_9834d3405aae447da47ed60d5c3d4d30 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                135,
                21,
                23,
                111,
                86,
                98,
                136
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb6B",
            "legendHoverLink": true,
            "data": [
                100,
                108,
                95,
                35,
                42,
                143,
                68
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A",
                "\u5546\u5bb6B"
            ],
            "selected": {
                "\u5546\u5bb6A": true,
                "\u5546\u5bb6B": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u886c\u886b",
                "\u6bdb\u8863",
                "\u9886\u5e26",
                "\u88e4\u5b50",
                "\u98ce\u8863",
                "\u9ad8\u8ddf\u978b",
                "\u889c\u5b50"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "\u4e3b\u6807\u9898",
            "subtext": "\u526f\u6807\u9898",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "type": "jpeg",
                "backgroundColor": "white",
                "connectedBackgroundColor": "#fff",
                "show": true,
                "title": "\u4fdd\u5b58\u4e3ajpeg",
                "pixelRatio": 10
            },
            "restore": {
                "show": true,
                "title": "\u8fd8\u539f"
            },
            "dataView": {
                "show": true,
                "title": "\u6570\u636e\u89c6\u56fe",
                "readOnly": false,
                "lang": [
                    "\u6570\u636e\u89c6\u56fe",
                    "\u5173\u95ed",
                    "\u5237\u65b0"
                ],
                "backgroundColor": "#fff",
                "textareaColor": "#fff",
                "textareaBorderColor": "#333",
                "textColor": "#000",
                "buttonColor": "#c23531",
                "buttonTextColor": "#fff"
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "\u533a\u57df\u7f29\u653e",
                    "back": "\u533a\u57df\u7f29\u653e\u8fd8\u539f"
                },
                "icon": {},
                "xAxisIndex": false,
                "yAxisIndex": false,
                "filterMode": "filter"
            },
            "magicType": {
                "show": true,
                "type": [
                    "line",
                    "bar",
                    "stack",
                    "tiled"
                ],
                "title": {
                    "line": "\u5207\u6362\u4e3a\u6298\u7ebf\u56fe",
                    "bar": "\u5207\u6362\u4e3a\u67f1\u72b6\u56fe",
                    "stack": "\u5207\u6362\u4e3a\u5806\u53e0",
                    "tiled": "\u5207\u6362\u4e3a\u5e73\u94fa"
                },
                "icon": {}
            },
            "brush": {
                "icon": {},
                "title": {
                    "rect": "\u77e9\u5f62\u9009\u62e9",
                    "polygon": "\u5708\u9009",
                    "lineX": "\u6a2a\u5411\u9009\u62e9",
                    "lineY": "\u7eb5\u5411\u9009\u62e9",
                    "keep": "\u4fdd\u6301\u9009\u62e9",
                    "clear": "\u6e05\u9664\u9009\u62e9"
                }
            }
        }
    }
};
        chart_9834d3405aae447da47ed60d5c3d4d30.setOption(option_9834d3405aae447da47ed60d5c3d4d30);
    </script>
</body>
</html>





```python
c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts={"text": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的"}
    )
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="1e52509676b64b83a399946b3ce6c078" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1e52509676b64b83a399946b3ce6c078 = echarts.init(
            document.getElementById('1e52509676b64b83a399946b3ce6c078'), 'macarons', {renderer: 'canvas'});
        var option_1e52509676b64b83a399946b3ce6c078 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                66,
                82,
                42,
                147,
                126,
                65,
                106
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb6B",
            "legendHoverLink": true,
            "data": [
                43,
                106,
                134,
                39,
                82,
                100,
                145
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A",
                "\u5546\u5bb6B"
            ],
            "selected": {
                "\u5546\u5bb6A": true,
                "\u5546\u5bb6B": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u54c8\u58eb\u5947",
                "\u8428\u6469\u8036",
                "\u6cf0\u8fea",
                "\u91d1\u6bdb",
                "\u7267\u7f8a\u72ac",
                "\u5409\u5a03\u5a03",
                "\u67ef\u57fa"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": {
        "text": "Bar-\u901a\u8fc7 dict \u8fdb\u884c\u914d\u7f6e",
        "subtext": "\u6211\u4e5f\u662f\u901a\u8fc7 dict \u8fdb\u884c\u914d\u7f6e\u7684"
    }
};
        chart_1e52509676b64b83a399946b3ce6c078.setOption(option_1e52509676b64b83a399946b3ce6c078);
    </script>
</body>
</html>





```python
c = (
    Bar(
        init_opts=opts.InitOpts(
            animation_opts=opts.AnimationOpts(
                animation_delay=1000, animation_easing="elasticOut"
            )
        )
    )
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-动画配置基本示例", subtitle="我是副标题"))
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="60bfae23c577400a8f5a640200dc5122" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_60bfae23c577400a8f5a640200dc5122 = echarts.init(
            document.getElementById('60bfae23c577400a8f5a640200dc5122'), 'white', {renderer: 'canvas'});
        var option_60bfae23c577400a8f5a640200dc5122 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "elasticOut",
    "animationDelay": 1000,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                105,
                45,
                138,
                146,
                112,
                96,
                97
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb6B",
            "legendHoverLink": true,
            "data": [
                81,
                83,
                73,
                104,
                102,
                100,
                114
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A",
                "\u5546\u5bb6B"
            ],
            "selected": {
                "\u5546\u5bb6A": true,
                "\u5546\u5bb6B": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u6cb3\u9a6c",
                "\u87d2\u86c7",
                "\u8001\u864e",
                "\u5927\u8c61",
                "\u5154\u5b50",
                "\u718a\u732b",
                "\u72ee\u5b50"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Bar-\u52a8\u753b\u914d\u7f6e\u57fa\u672c\u793a\u4f8b",
            "subtext": "\u6211\u662f\u526f\u6807\u9898",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_60bfae23c577400a8f5a640200dc5122.setOption(option_60bfae23c577400a8f5a640200dc5122);
    </script>
</body>
</html>





```python
c = (
    Bar(
        init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"}
        )
    )
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Bar-背景图基本示例",
            subtitle="我是副标题",
            title_textstyle_opts=opts.TextStyleOpts(color="white"),
        )
    )
)
c.add_js_funcs(
    """
    var img = new Image(); img.src = 'https://s2.ax1x.com/2019/07/08/ZsS0fK.jpg';
    """
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="f3bb7ff0c6314a6bafe859da6705d30c" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_f3bb7ff0c6314a6bafe859da6705d30c = echarts.init(
            document.getElementById('f3bb7ff0c6314a6bafe859da6705d30c'), 'white', {renderer: 'canvas'});

    var img = new Image(); img.src = 'https://s2.ax1x.com/2019/07/08/ZsS0fK.jpg';

        var option_f3bb7ff0c6314a6bafe859da6705d30c = {
    "backgroundColor": {
        "type": "pattern",
        "image": img,
        "repeat": "no-repeat"
    },
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                68,
                108,
                130,
                71,
                52,
                109,
                71
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb6B",
            "legendHoverLink": true,
            "data": [
                25,
                36,
                108,
                72,
                81,
                94,
                77
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A",
                "\u5546\u5bb6B"
            ],
            "selected": {
                "\u5546\u5bb6A": true,
                "\u5546\u5bb6B": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u5468\u4e00",
                "\u5468\u4e8c",
                "\u5468\u4e09",
                "\u5468\u56db",
                "\u5468\u4e94",
                "\u5468\u516d",
                "\u5468\u65e5"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Bar-\u80cc\u666f\u56fe\u57fa\u672c\u793a\u4f8b",
            "subtext": "\u6211\u662f\u526f\u6807\u9898",
            "padding": 5,
            "itemGap": 10,
            "textStyle": {
                "color": "white"
            }
        }
    ]
};
        chart_f3bb7ff0c6314a6bafe859da6705d30c.setOption(option_f3bb7ff0c6314a6bafe859da6705d30c);
    </script>
</body>
</html>





```python
c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-渐变圆柱"))
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="e4e38b47fdcb4b9bbd322626eba2324a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_e4e38b47fdcb4b9bbd322626eba2324a = echarts.init(
            document.getElementById('e4e38b47fdcb4b9bbd322626eba2324a'), 'white', {renderer: 'canvas'});
        var option_e4e38b47fdcb4b9bbd322626eba2324a = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                93,
                92,
                104,
                105,
                93,
                101,
                98
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "60%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "itemStyle": {
                "normal": {
                    "color": new echarts.graphic.LinearGradient(0, 0, 0, 1, [{                offset: 0,                color: 'rgba(0, 244, 255, 1)'            }, {                offset: 1,                color: 'rgba(0, 77, 167, 1)'            }], false),
                    "barBorderRadius": [
                        30,
                        30,
                        30,
                        30
                    ],
                    "shadowColor": "rgb(0, 160, 221)"
                }
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A"
            ],
            "selected": {
                "\u5546\u5bb6A": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u886c\u886b",
                "\u6bdb\u8863",
                "\u9886\u5e26",
                "\u88e4\u5b50",
                "\u98ce\u8863",
                "\u9ad8\u8ddf\u978b",
                "\u889c\u5b50"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Bar-\u6e10\u53d8\u5706\u67f1",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_e4e38b47fdcb4b9bbd322626eba2324a.setOption(option_e4e38b47fdcb4b9bbd322626eba2324a);
    </script>
</body>
</html>





```python
category = ["类目{}".format(i) for i in range(0, 100)]
red_bar = [
    0,
    -8.901463875624668,
    -17.025413764148556,
    -24.038196249566663,
    -29.66504684804471,
    -33.699527649688676,
    -36.00971978255796,
    -36.541005056170455,
    -35.31542466107655,
    -32.427752866005996,
    -28.038563739693934,
    -22.364693082297347,
    -15.667600860943732,
    -8.240217424060843,
    -0.3929067389459173,
    7.560799717904647,
    15.318054209871054,
    22.599523033552096,
    29.16065418543528,
    34.800927952557615,
    39.37074152590451,
    42.77569739999406,
    44.97819140223978,
    45.99632376477021,
    45.900279829731865,
    44.806440199911805,
    42.86957840395034,
    40.2735832137877,
    37.22119936652441,
    33.92331243435557,
    30.588309963978517,
    27.412031986865767,
    24.56878097935778,
    22.203796820272576,
    20.427519715115604,
    19.311867685884827,
    18.888649906111855,
    19.150128087782186,
    20.051630602288828,
    21.516023200879346,
    23.439750867099516,
    25.700091656548704,
    28.163208735293757,
    30.692553648214542,
    33.1571635093161,
    35.439407573791215,
    37.44177367693234,
    39.09234039030659,
    40.34865356244595,
    41.19981246258526,
    41.66666666666667,
    41.80012531240646,
    41.67768039516203,
    41.39834040182826,
    41.07625507973403,
    40.833382300579814,
    40.79160029175877,
    41.06470032034727,
    41.75070457358366,
    42.924940903672564,
    44.63427081999565,
    46.89281122872821,
    49.679416561286956,
    52.93709961387478,
    56.574470884754874,
    60.46917221906629,
    64.47317623531558,
    68.41972346252496,
    72.1315793340836,
    75.43021771943799,
    78.14548044723074,
    80.12522637371026,
    81.24447108408411,
    81.41353029256493,
    80.58471628367427,
    78.75719600392792,
    75.97969924353211,
    72.35086229880064,
    68.01710226438443,
    63.16803467673056,
    58.029567166714706,
    52.854918421647554,
    47.91391949819902,
    43.48104807503482,
    39.82272085822884,
    37.18442111754884,
    35.778264289169215,
    35.77160292258658,
    37.27724241244461,
    40.345781666728996,
    44.96051012913295,
    51.035187614675685,
    58.41491053964701,
    66.8801325453253,
    76.15376513468516,
    85.91114110149952,
    95.79248672571518,
    105.41742429574506,
    114.40092042993717,
    122.37001313784816,
]
blue_bar = [
    -50,
    -47.18992898088751,
    -42.54426104547181,
    -36.290773900754886,
    -28.71517529663627,
    -20.146937097399626,
    -10.94374119697364,
    -1.4752538113770308,
    7.893046603320797,
    16.81528588241657,
    24.979206795219028,
    32.11821023962515,
    38.02096119056733,
    42.53821720798438,
    45.58667093073836,
    47.14973738101559,
    47.275355710354944,
    46.07100702178889,
    43.6962693226927,
    40.35333240268025,
    36.275975292575026,
    31.71756381888028,
    26.938653692729076,
    22.194784893913152,
    17.725026430574392,
    13.741778696752679,
    10.422266555457615,
    7.902063853319403,
    6.270884006107842,
    5.570756810898967,
    5.796594266992678,
    6.899033489892203,
    8.7893381290192,
    11.346045936704996,
    14.42297348773613,
    17.858132851517098,
    21.483081596548438,
    25.132218074866262,
    28.651548555679597,
    31.906490373810854,
    34.788333671419466,
    37.21906041552118,
    39.154309232933485,
    40.58437366457342,
    41.5332247510366,
    42.05565130942339,
    42.23270781895,
    42.165745792772285,
    41.969375711588256,
    41.76375960543808,
    41.66666666666667,
    41.7857343479728,
    42.21136481847887,
    43.01065209435119,
    44.22268037417866,
    45.855461823273586,
    47.88469584957917,
    50.25443606443524,
    52.879650371477126,
    55.650558977584225,
    58.43853958732492,
    61.10330341815434,
    63.500974294013034,
    65.49264961151306,
    66.95298925309743,
    67.77836838841961,
    67.89414332224722,
    67.26061575374229,
    65.87733853082335,
    63.785482681031894,
    61.068077697490004,
    57.84804048526095,
    54.284018163297375,
    50.564180830851214,
    46.89820707575337,
    43.50780217852947,
    40.616171775045245,
    38.4369379107128,
    37.16302649485318,
    36.95607267600796,
    37.93688225696513,
    40.17745279877072,
    43.694998595987045,
    48.44834150353593,
    54.33692802801367,
    61.20261650152743,
    68.83425165632042,
    76.97491319735354,
    85.33159602026458,
    93.58695857541488,
    101.4126683297632,
    108.48378461530217,
    114.49355390682695,
    119.16795429637915,
    122.27931702317058,
    123.65837448506679,
    123.20413594805603,
    120.89107255501017,
    116.7731992576505,
    110.98476877890735,
]


c= (
    Bar()
    .add_xaxis(xaxis_data=category)
    .add_yaxis(
        series_name="bar", y_axis=red_bar, label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name="bar2",
        y_axis=blue_bar,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="柱状图动画延迟"),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
   
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="1e9307ea0baa4db6a5465a596d167ed1" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1e9307ea0baa4db6a5465a596d167ed1 = echarts.init(
            document.getElementById('1e9307ea0baa4db6a5465a596d167ed1'), 'white', {renderer: 'canvas'});
        var option_1e9307ea0baa4db6a5465a596d167ed1 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "bar",
            "legendHoverLink": true,
            "data": [
                0,
                -8.901463875624668,
                -17.025413764148556,
                -24.038196249566663,
                -29.66504684804471,
                -33.699527649688676,
                -36.00971978255796,
                -36.541005056170455,
                -35.31542466107655,
                -32.427752866005996,
                -28.038563739693934,
                -22.364693082297347,
                -15.667600860943732,
                -8.240217424060843,
                -0.3929067389459173,
                7.560799717904647,
                15.318054209871054,
                22.599523033552096,
                29.16065418543528,
                34.800927952557615,
                39.37074152590451,
                42.77569739999406,
                44.97819140223978,
                45.99632376477021,
                45.900279829731865,
                44.806440199911805,
                42.86957840395034,
                40.2735832137877,
                37.22119936652441,
                33.92331243435557,
                30.588309963978517,
                27.412031986865767,
                24.56878097935778,
                22.203796820272576,
                20.427519715115604,
                19.311867685884827,
                18.888649906111855,
                19.150128087782186,
                20.051630602288828,
                21.516023200879346,
                23.439750867099516,
                25.700091656548704,
                28.163208735293757,
                30.692553648214542,
                33.1571635093161,
                35.439407573791215,
                37.44177367693234,
                39.09234039030659,
                40.34865356244595,
                41.19981246258526,
                41.66666666666667,
                41.80012531240646,
                41.67768039516203,
                41.39834040182826,
                41.07625507973403,
                40.833382300579814,
                40.79160029175877,
                41.06470032034727,
                41.75070457358366,
                42.924940903672564,
                44.63427081999565,
                46.89281122872821,
                49.679416561286956,
                52.93709961387478,
                56.574470884754874,
                60.46917221906629,
                64.47317623531558,
                68.41972346252496,
                72.1315793340836,
                75.43021771943799,
                78.14548044723074,
                80.12522637371026,
                81.24447108408411,
                81.41353029256493,
                80.58471628367427,
                78.75719600392792,
                75.97969924353211,
                72.35086229880064,
                68.01710226438443,
                63.16803467673056,
                58.029567166714706,
                52.854918421647554,
                47.91391949819902,
                43.48104807503482,
                39.82272085822884,
                37.18442111754884,
                35.778264289169215,
                35.77160292258658,
                37.27724241244461,
                40.345781666728996,
                44.96051012913295,
                51.035187614675685,
                58.41491053964701,
                66.8801325453253,
                76.15376513468516,
                85.91114110149952,
                95.79248672571518,
                105.41742429574506,
                114.40092042993717,
                122.37001313784816
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "bar",
            "name": "bar2",
            "legendHoverLink": true,
            "data": [
                -50,
                -47.18992898088751,
                -42.54426104547181,
                -36.290773900754886,
                -28.71517529663627,
                -20.146937097399626,
                -10.94374119697364,
                -1.4752538113770308,
                7.893046603320797,
                16.81528588241657,
                24.979206795219028,
                32.11821023962515,
                38.02096119056733,
                42.53821720798438,
                45.58667093073836,
                47.14973738101559,
                47.275355710354944,
                46.07100702178889,
                43.6962693226927,
                40.35333240268025,
                36.275975292575026,
                31.71756381888028,
                26.938653692729076,
                22.194784893913152,
                17.725026430574392,
                13.741778696752679,
                10.422266555457615,
                7.902063853319403,
                6.270884006107842,
                5.570756810898967,
                5.796594266992678,
                6.899033489892203,
                8.7893381290192,
                11.346045936704996,
                14.42297348773613,
                17.858132851517098,
                21.483081596548438,
                25.132218074866262,
                28.651548555679597,
                31.906490373810854,
                34.788333671419466,
                37.21906041552118,
                39.154309232933485,
                40.58437366457342,
                41.5332247510366,
                42.05565130942339,
                42.23270781895,
                42.165745792772285,
                41.969375711588256,
                41.76375960543808,
                41.66666666666667,
                41.7857343479728,
                42.21136481847887,
                43.01065209435119,
                44.22268037417866,
                45.855461823273586,
                47.88469584957917,
                50.25443606443524,
                52.879650371477126,
                55.650558977584225,
                58.43853958732492,
                61.10330341815434,
                63.500974294013034,
                65.49264961151306,
                66.95298925309743,
                67.77836838841961,
                67.89414332224722,
                67.26061575374229,
                65.87733853082335,
                63.785482681031894,
                61.068077697490004,
                57.84804048526095,
                54.284018163297375,
                50.564180830851214,
                46.89820707575337,
                43.50780217852947,
                40.616171775045245,
                38.4369379107128,
                37.16302649485318,
                36.95607267600796,
                37.93688225696513,
                40.17745279877072,
                43.694998595987045,
                48.44834150353593,
                54.33692802801367,
                61.20261650152743,
                68.83425165632042,
                76.97491319735354,
                85.33159602026458,
                93.58695857541488,
                101.4126683297632,
                108.48378461530217,
                114.49355390682695,
                119.16795429637915,
                122.27931702317058,
                123.65837448506679,
                123.20413594805603,
                120.89107255501017,
                116.7731992576505,
                110.98476877890735
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "bar",
                "bar2"
            ],
            "selected": {
                "bar": true,
                "bar2": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u7c7b\u76ee0",
                "\u7c7b\u76ee1",
                "\u7c7b\u76ee2",
                "\u7c7b\u76ee3",
                "\u7c7b\u76ee4",
                "\u7c7b\u76ee5",
                "\u7c7b\u76ee6",
                "\u7c7b\u76ee7",
                "\u7c7b\u76ee8",
                "\u7c7b\u76ee9",
                "\u7c7b\u76ee10",
                "\u7c7b\u76ee11",
                "\u7c7b\u76ee12",
                "\u7c7b\u76ee13",
                "\u7c7b\u76ee14",
                "\u7c7b\u76ee15",
                "\u7c7b\u76ee16",
                "\u7c7b\u76ee17",
                "\u7c7b\u76ee18",
                "\u7c7b\u76ee19",
                "\u7c7b\u76ee20",
                "\u7c7b\u76ee21",
                "\u7c7b\u76ee22",
                "\u7c7b\u76ee23",
                "\u7c7b\u76ee24",
                "\u7c7b\u76ee25",
                "\u7c7b\u76ee26",
                "\u7c7b\u76ee27",
                "\u7c7b\u76ee28",
                "\u7c7b\u76ee29",
                "\u7c7b\u76ee30",
                "\u7c7b\u76ee31",
                "\u7c7b\u76ee32",
                "\u7c7b\u76ee33",
                "\u7c7b\u76ee34",
                "\u7c7b\u76ee35",
                "\u7c7b\u76ee36",
                "\u7c7b\u76ee37",
                "\u7c7b\u76ee38",
                "\u7c7b\u76ee39",
                "\u7c7b\u76ee40",
                "\u7c7b\u76ee41",
                "\u7c7b\u76ee42",
                "\u7c7b\u76ee43",
                "\u7c7b\u76ee44",
                "\u7c7b\u76ee45",
                "\u7c7b\u76ee46",
                "\u7c7b\u76ee47",
                "\u7c7b\u76ee48",
                "\u7c7b\u76ee49",
                "\u7c7b\u76ee50",
                "\u7c7b\u76ee51",
                "\u7c7b\u76ee52",
                "\u7c7b\u76ee53",
                "\u7c7b\u76ee54",
                "\u7c7b\u76ee55",
                "\u7c7b\u76ee56",
                "\u7c7b\u76ee57",
                "\u7c7b\u76ee58",
                "\u7c7b\u76ee59",
                "\u7c7b\u76ee60",
                "\u7c7b\u76ee61",
                "\u7c7b\u76ee62",
                "\u7c7b\u76ee63",
                "\u7c7b\u76ee64",
                "\u7c7b\u76ee65",
                "\u7c7b\u76ee66",
                "\u7c7b\u76ee67",
                "\u7c7b\u76ee68",
                "\u7c7b\u76ee69",
                "\u7c7b\u76ee70",
                "\u7c7b\u76ee71",
                "\u7c7b\u76ee72",
                "\u7c7b\u76ee73",
                "\u7c7b\u76ee74",
                "\u7c7b\u76ee75",
                "\u7c7b\u76ee76",
                "\u7c7b\u76ee77",
                "\u7c7b\u76ee78",
                "\u7c7b\u76ee79",
                "\u7c7b\u76ee80",
                "\u7c7b\u76ee81",
                "\u7c7b\u76ee82",
                "\u7c7b\u76ee83",
                "\u7c7b\u76ee84",
                "\u7c7b\u76ee85",
                "\u7c7b\u76ee86",
                "\u7c7b\u76ee87",
                "\u7c7b\u76ee88",
                "\u7c7b\u76ee89",
                "\u7c7b\u76ee90",
                "\u7c7b\u76ee91",
                "\u7c7b\u76ee92",
                "\u7c7b\u76ee93",
                "\u7c7b\u76ee94",
                "\u7c7b\u76ee95",
                "\u7c7b\u76ee96",
                "\u7c7b\u76ee97",
                "\u7c7b\u76ee98",
                "\u7c7b\u76ee99"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisTick": {
                "show": true,
                "alignWithLabel": false,
                "inside": false
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": true,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "\u67f1\u72b6\u56fe\u52a8\u753b\u5ef6\u8fdf",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_1e9307ea0baa4db6a5465a596d167ed1.setOption(option_1e9307ea0baa4db6a5465a596d167ed1);
    </script>
</body>
</html>





```python
color_function = """
        function (params) {
            if (params.value > 0 && params.value < 50) {
                return 'red';
            } else if (params.value > 50 && params.value < 100) {
                return 'blue';
            }
            return 'green';
        }
        """
c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "商家A",
        Faker.values(),
        itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)),
    )
    .add_yaxis(
        "商家B",
        Faker.values(),
        itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)),
    )
    .add_yaxis(
        "商家C",
        Faker.values(),
        itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-自定义柱状颜色"))
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="17d77e454aa343d0a7319a22de46b2c9" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_17d77e454aa343d0a7319a22de46b2c9 = echarts.init(
            document.getElementById('17d77e454aa343d0a7319a22de46b2c9'), 'white', {renderer: 'canvas'});
        var option_17d77e454aa343d0a7319a22de46b2c9 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                87,
                117,
                137,
                89,
                93,
                40,
                98
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "itemStyle": {
                "color":         function (params) {            if (params.value > 0 && params.value < 50) {                return 'red';            } else if (params.value > 50 && params.value < 100) {                return 'blue';            }            return 'green';        }        
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb6B",
            "legendHoverLink": true,
            "data": [
                127,
                150,
                101,
                111,
                78,
                139,
                82
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "itemStyle": {
                "color":         function (params) {            if (params.value > 0 && params.value < 50) {                return 'red';            } else if (params.value > 50 && params.value < 100) {                return 'blue';            }            return 'green';        }        
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb6C",
            "legendHoverLink": true,
            "data": [
                82,
                58,
                101,
                60,
                150,
                107,
                84
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "itemStyle": {
                "color":         function (params) {            if (params.value > 0 && params.value < 50) {                return 'red';            } else if (params.value > 50 && params.value < 100) {                return 'blue';            }            return 'green';        }        
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A",
                "\u5546\u5bb6B",
                "\u5546\u5bb6C"
            ],
            "selected": {
                "\u5546\u5bb6A": true,
                "\u5546\u5bb6B": true,
                "\u5546\u5bb6C": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u54c8\u58eb\u5947",
                "\u8428\u6469\u8036",
                "\u6cf0\u8fea",
                "\u91d1\u6bdb",
                "\u7267\u7f8a\u72ac",
                "\u5409\u5a03\u5a03",
                "\u67ef\u57fa"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Bar-\u81ea\u5b9a\u4e49\u67f1\u72b6\u989c\u8272",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_17d77e454aa343d0a7319a22de46b2c9.setOption(option_17d77e454aa343d0a7319a22de46b2c9);
    </script>
</body>
</html>





```python
c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
    )
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="4eb432bba02744f08c0f89fa77ff0fea" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_4eb432bba02744f08c0f89fa77ff0fea = echarts.init(
            document.getElementById('4eb432bba02744f08c0f89fa77ff0fea'), 'white', {renderer: 'canvas'});
        var option_4eb432bba02744f08c0f89fa77ff0fea = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#444693",
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                2,
                22,
                13,
                14,
                15,
                15,
                24,
                2,
                27,
                28,
                8,
                29,
                26,
                16,
                19,
                3,
                1,
                29,
                7,
                12,
                11,
                18,
                14,
                1,
                14,
                25,
                25,
                14,
                5,
                23
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A"
            ],
            "selected": {
                "\u5546\u5bb6A": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "0\u5929",
                "1\u5929",
                "2\u5929",
                "3\u5929",
                "4\u5929",
                "5\u5929",
                "6\u5929",
                "7\u5929",
                "8\u5929",
                "9\u5929",
                "10\u5929",
                "11\u5929",
                "12\u5929",
                "13\u5929",
                "14\u5929",
                "15\u5929",
                "16\u5929",
                "17\u5929",
                "18\u5929",
                "19\u5929",
                "20\u5929",
                "21\u5929",
                "22\u5929",
                "23\u5929",
                "24\u5929",
                "25\u5929",
                "26\u5929",
                "27\u5929",
                "28\u5929",
                "29\u5929"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Bar-DataZoom\uff08slider+inside\uff09",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "dataZoom": [
        {
            "show": true,
            "type": "slider",
            "realtime": true,
            "start": 20,
            "end": 80,
            "orient": "horizontal",
            "zoomLock": false,
            "filterMode": "filter"
        },
        {
            "show": true,
            "type": "inside",
            "realtime": true,
            "start": 20,
            "end": 80,
            "orient": "horizontal",
            "zoomLock": false,
            "filterMode": "filter"
        }
    ]
};
        chart_4eb432bba02744f08c0f89fa77ff0fea.setOption(option_4eb432bba02744f08c0f89fa77ff0fea);
    </script>
</body>
</html>





```python
c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),
        datazoom_opts=opts.DataZoomOpts(type_="inside"),
    )
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="1980e8173e634f81a694e4d2edf3b0b6" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1980e8173e634f81a694e4d2edf3b0b6 = echarts.init(
            document.getElementById('1980e8173e634f81a694e4d2edf3b0b6'), 'white', {renderer: 'canvas'});
        var option_1980e8173e634f81a694e4d2edf3b0b6 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#546570",
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                2,
                22,
                13,
                14,
                15,
                15,
                24,
                2,
                27,
                28,
                8,
                29,
                26,
                16,
                19,
                3,
                1,
                29,
                7,
                12,
                11,
                18,
                14,
                1,
                14,
                25,
                25,
                14,
                5,
                23
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A"
            ],
            "selected": {
                "\u5546\u5bb6A": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "0\u5929",
                "1\u5929",
                "2\u5929",
                "3\u5929",
                "4\u5929",
                "5\u5929",
                "6\u5929",
                "7\u5929",
                "8\u5929",
                "9\u5929",
                "10\u5929",
                "11\u5929",
                "12\u5929",
                "13\u5929",
                "14\u5929",
                "15\u5929",
                "16\u5929",
                "17\u5929",
                "18\u5929",
                "19\u5929",
                "20\u5929",
                "21\u5929",
                "22\u5929",
                "23\u5929",
                "24\u5929",
                "25\u5929",
                "26\u5929",
                "27\u5929",
                "28\u5929",
                "29\u5929"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Bar-DataZoom\uff08inside\uff09",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "dataZoom": {
        "show": true,
        "type": "inside",
        "realtime": true,
        "start": 20,
        "end": 80,
        "orient": "horizontal",
        "zoomLock": false,
        "filterMode": "filter"
    }
};
        chart_1980e8173e634f81a694e4d2edf3b0b6.setOption(option_1980e8173e634f81a694e4d2edf3b0b6);
    </script>
</body>
</html>





```python
c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
        datazoom_opts=opts.DataZoomOpts(orient='vertical'),  # vertical   horizontal
    )
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="1f16044d5bb048f49b7752757acdd3c9" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1f16044d5bb048f49b7752757acdd3c9 = echarts.init(
            document.getElementById('1f16044d5bb048f49b7752757acdd3c9'), 'white', {renderer: 'canvas'});
        var option_1f16044d5bb048f49b7752757acdd3c9 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb6A",
            "legendHoverLink": true,
            "data": [
                2,
                22,
                13,
                14,
                15,
                15,
                24,
                2,
                27,
                28,
                8,
                29,
                26,
                16,
                19,
                3,
                1,
                29,
                7,
                12,
                11,
                18,
                14,
                1,
                14,
                25,
                25,
                14,
                5,
                23
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb6A"
            ],
            "selected": {
                "\u5546\u5bb6A": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "0\u5929",
                "1\u5929",
                "2\u5929",
                "3\u5929",
                "4\u5929",
                "5\u5929",
                "6\u5929",
                "7\u5929",
                "8\u5929",
                "9\u5929",
                "10\u5929",
                "11\u5929",
                "12\u5929",
                "13\u5929",
                "14\u5929",
                "15\u5929",
                "16\u5929",
                "17\u5929",
                "18\u5929",
                "19\u5929",
                "20\u5929",
                "21\u5929",
                "22\u5929",
                "23\u5929",
                "24\u5929",
                "25\u5929",
                "26\u5929",
                "27\u5929",
                "28\u5929",
                "29\u5929"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Bar-DataZoom\uff08slider-\u6c34\u5e73\uff09",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "dataZoom": {
        "show": true,
        "type": "slider",
        "realtime": true,
        "start": 20,
        "end": 80,
        "orient": "vertical",
        "zoomLock": false,
        "filterMode": "filter"
    }
};
        chart_1f16044d5bb048f49b7752757acdd3c9.setOption(option_1f16044d5bb048f49b7752757acdd3c9);
    </script>
</body>
</html>





```python
list2 = [
    {"value": 12, "percent": 12 / (12 + 3)},
    {"value": 23, "percent": 23 / (23 + 21)},
    {"value": 33, "percent": 33 / (33 + 5)},
    {"value": 3, "percent": 3 / (3 + 52)},
    {"value": 33, "percent": 33 / (33 + 43)},
]

list3 = [
    {"value": 3, "percent": 3 / (12 + 3)},
    {"value": 21, "percent": 21 / (23 + 21)},
    {"value": 5, "percent": 5 / (33 + 5)},
    {"value": 52, "percent": 52 / (3 + 52)},
    {"value": 43, "percent": 43 / (33 + 43)},
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([1, 2, 3, 4, 5])
    .add_yaxis("product1", list2, stack="stack1", category_gap="50%")
    .add_yaxis("product2", list3, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )

)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="1858124d663e4b17b22809879eda932e" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1858124d663e4b17b22809879eda932e = echarts.init(
            document.getElementById('1858124d663e4b17b22809879eda932e'), 'light', {renderer: 'canvas'});
        var option_1858124d663e4b17b22809879eda932e = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "series": [
        {
            "type": "bar",
            "name": "product1",
            "legendHoverLink": true,
            "data": [
                {
                    "value": 12,
                    "percent": 0.8
                },
                {
                    "value": 23,
                    "percent": 0.5227272727272727
                },
                {
                    "value": 33,
                    "percent": 0.868421052631579
                },
                {
                    "value": 3,
                    "percent": 0.05454545454545454
                },
                {
                    "value": 33,
                    "percent": 0.4342105263157895
                }
            ],
            "showBackground": false,
            "stack": "stack1",
            "barMinHeight": 0,
            "barCategoryGap": "50%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "right",
                "margin": 8,
                "formatter": function(x){return Number(x.data.percent * 100).toFixed() + '%';}
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        },
        {
            "type": "bar",
            "name": "product2",
            "legendHoverLink": true,
            "data": [
                {
                    "value": 3,
                    "percent": 0.2
                },
                {
                    "value": 21,
                    "percent": 0.4772727272727273
                },
                {
                    "value": 5,
                    "percent": 0.13157894736842105
                },
                {
                    "value": 52,
                    "percent": 0.9454545454545454
                },
                {
                    "value": 43,
                    "percent": 0.5657894736842105
                }
            ],
            "showBackground": false,
            "stack": "stack1",
            "barMinHeight": 0,
            "barCategoryGap": "50%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "right",
                "margin": 8,
                "formatter": function(x){return Number(x.data.percent * 100).toFixed() + '%';}
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                "product1",
                "product2"
            ],
            "selected": {
                "product1": true,
                "product2": true
            }
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                1,
                2,
                3,
                4,
                5
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ]
};
        chart_1858124d663e4b17b22809879eda932e.setOption(option_1858124d663e4b17b22809879eda932e);
    </script>
</body>
</html>





```python
x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

bar = (
    Bar()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="蒸发量",
        y_axis=[2.0,4.9,7.0,23.2,25.6,76.7,135.6,162.2,32.6,20.0,6.4,3.3,],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="降水量",
        y_axis=[2.6,5.9,9.0, 26.4,28.7, 70.7, 175.6,182.2,48.7,18.8, 6.0, 2.3,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="温度",
            type_="value",
            min_=0,
            max_=25,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="水量",
            type_="value",
            min_=0,
            max_=250,
            interval=50,
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)

line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="平均温度",
        yaxis_index=1,
        y_axis=[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line).render_notebook()

```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="8e16635e49fe4941b021b8b6ce2c9d9f" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_8e16635e49fe4941b021b8b6ce2c9d9f = echarts.init(
            document.getElementById('8e16635e49fe4941b021b8b6ce2c9d9f'), 'white', {renderer: 'canvas'});
        var option_8e16635e49fe4941b021b8b6ce2c9d9f = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u84b8\u53d1\u91cf",
            "legendHoverLink": true,
            "data": [
                2.0,
                4.9,
                7.0,
                23.2,
                25.6,
                76.7,
                135.6,
                162.2,
                32.6,
                20.0,
                6.4,
                3.3
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "bar",
            "name": "\u964d\u6c34\u91cf",
            "legendHoverLink": true,
            "data": [
                2.6,
                5.9,
                9.0,
                26.4,
                28.7,
                70.7,
                175.6,
                182.2,
                48.7,
                18.8,
                6.0,
                2.3
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "line",
            "name": "\u5e73\u5747\u6e29\u5ea6",
            "connectNulls": false,
            "yAxisIndex": 1,
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "clip": true,
            "step": false,
            "data": [
                [
                    "1\u6708",
                    2.0
                ],
                [
                    "2\u6708",
                    2.2
                ],
                [
                    "3\u6708",
                    3.3
                ],
                [
                    "4\u6708",
                    4.5
                ],
                [
                    "5\u6708",
                    6.3
                ],
                [
                    "6\u6708",
                    10.2
                ],
                [
                    "7\u6708",
                    20.3
                ],
                [
                    "8\u6708",
                    23.4
                ],
                [
                    "9\u6708",
                    23.0
                ],
                [
                    "10\u6708",
                    16.5
                ],
                [
                    "11\u6708",
                    12.0
                ],
                [
                    "12\u6708",
                    6.2
                ]
            ],
            "hoverAnimation": true,
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "show": true,
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            },
            "zlevel": 0,
            "z": 0
        }
    ],
    "legend": [
        {
            "data": [
                "\u84b8\u53d1\u91cf",
                "\u964d\u6c34\u91cf",
                "\u5e73\u5747\u6e29\u5ea6"
            ],
            "selected": {
                "\u84b8\u53d1\u91cf": true,
                "\u964d\u6c34\u91cf": true,
                "\u5e73\u5747\u6e29\u5ea6": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "axis",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "cross"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "type": "category",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisPointer": {
                "show": true,
                "type": "shadow"
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "1\u6708",
                "2\u6708",
                "3\u6708",
                "4\u6708",
                "5\u6708",
                "6\u6708",
                "7\u6708",
                "8\u6708",
                "9\u6708",
                "10\u6708",
                "11\u6708",
                "12\u6708"
            ]
        }
    ],
    "yAxis": [
        {
            "type": "value",
            "name": "\u6c34\u91cf",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "interval": 50,
            "gridIndex": 0,
            "axisTick": {
                "show": true,
                "alignWithLabel": false,
                "inside": false
            },
            "axisLabel": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{value} ml"
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "min": 0,
            "max": 250,
            "minInterval": 0,
            "splitLine": {
                "show": true,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        },
        {
            "type": "value",
            "name": "\u6e29\u5ea6",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "interval": 5,
            "gridIndex": 0,
            "axisLabel": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{value} \u00b0C"
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "min": 0,
            "max": 25,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_8e16635e49fe4941b021b8b6ce2c9d9f.setOption(option_8e16635e49fe4941b021b8b6ce2c9d9f);
    </script>
</body>
</html>





```python

x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
legend_list = ["蒸发量", "降水量", "平均温度"]
evaporation_capacity = [
    2.0,
    4.9,
    7.0,
    23.2,
    25.6,
    76.7,
    135.6,
    162.2,
    32.6,
    20.0,
    6.4,
    3.3,
]
rainfall_capacity = [
    2.6,
    5.9,
    9.0,
    26.4,
    28.7,
    70.7,
    175.6,
    182.2,
    48.7,
    18.8,
    6.0,
    2.3,
]
average_temperature = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

bar = (
    Bar(init_opts=opts.InitOpts(width="1260px", height="720px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="蒸发量",
        y_axis=evaporation_capacity,
        yaxis_index=0,
#         color=colors[0],
    )
    .add_yaxis(
        series_name="降水量", y_axis=rainfall_capacity, yaxis_index=1,
#         color=colors[1]
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="蒸发量",
            type_="value",
            min_=0,
            max_=250,
            position="left",
            axisline_opts=opts.AxisLineOpts(
#                 linestyle_opts=opts.LineStyleOpts(color=colors[1])
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="温度",
            min_=0,
            max_=25,
            position="right",
            axisline_opts=opts.AxisLineOpts(
#                 linestyle_opts=opts.LineStyleOpts(color=colors[2])
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
         xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="降水量",
            min_=0,
            max_=250,
            position="left",
            offset=80,
            axisline_opts=opts.AxisLineOpts(
#                 linestyle_opts=opts.LineStyleOpts(color=colors[0])
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        
    )
)

line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="平均温度", y_axis=average_temperature, yaxis_index=2, label_opts=opts.LabelOpts(is_show=True))

)
# bar.render_notebook()
# line.render_notebook()
bar.overlap(line).render_notebook()
# bar.overlap(line).render()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="b5820dae5a0744c4a4ae315d9b2037b0" class="chart-container" style="width:1260px; height:720px;"></div>
    <script>
        var chart_b5820dae5a0744c4a4ae315d9b2037b0 = echarts.init(
            document.getElementById('b5820dae5a0744c4a4ae315d9b2037b0'), 'white', {renderer: 'canvas'});
        var option_b5820dae5a0744c4a4ae315d9b2037b0 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u84b8\u53d1\u91cf",
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                2.0,
                4.9,
                7.0,
                23.2,
                25.6,
                76.7,
                135.6,
                162.2,
                32.6,
                20.0,
                6.4,
                3.3
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "bar",
            "name": "\u964d\u6c34\u91cf",
            "yAxisIndex": 1,
            "legendHoverLink": true,
            "data": [
                2.6,
                5.9,
                9.0,
                26.4,
                28.7,
                70.7,
                175.6,
                182.2,
                48.7,
                18.8,
                6.0,
                2.3
            ],
            "showBackground": false,
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        },
        {
            "type": "line",
            "name": "\u5e73\u5747\u6e29\u5ea6",
            "connectNulls": false,
            "yAxisIndex": 2,
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "clip": true,
            "step": false,
            "data": [
                [
                    "1\u6708",
                    2.0
                ],
                [
                    "2\u6708",
                    2.2
                ],
                [
                    "3\u6708",
                    3.3
                ],
                [
                    "4\u6708",
                    4.5
                ],
                [
                    "5\u6708",
                    6.3
                ],
                [
                    "6\u6708",
                    10.2
                ],
                [
                    "7\u6708",
                    20.3
                ],
                [
                    "8\u6708",
                    23.4
                ],
                [
                    "9\u6708",
                    23.0
                ],
                [
                    "10\u6708",
                    16.5
                ],
                [
                    "11\u6708",
                    12.0
                ],
                [
                    "12\u6708",
                    6.2
                ]
            ],
            "hoverAnimation": true,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "show": true,
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            },
            "zlevel": 0,
            "z": 0
        }
    ],
    "legend": [
        {
            "data": [
                "\u84b8\u53d1\u91cf",
                "\u964d\u6c34\u91cf",
                "\u5e73\u5747\u6e29\u5ea6"
            ],
            "selected": {
                "\u84b8\u53d1\u91cf": true,
                "\u964d\u6c34\u91cf": true,
                "\u5e73\u5747\u6e29\u5ea6": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "axis",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "cross"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "type": "category",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisPointer": {
                "show": true,
                "type": "shadow"
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "1\u6708",
                "2\u6708",
                "3\u6708",
                "4\u6708",
                "5\u6708",
                "6\u6708",
                "7\u6708",
                "8\u6708",
                "9\u6708",
                "10\u6708",
                "11\u6708",
                "12\u6708"
            ]
        }
    ],
    "yAxis": [
        {
            "type": "value",
            "name": "\u964d\u6c34\u91cf",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLine": {
                "show": true,
                "onZero": true,
                "onZeroAxisIndex": 0
            },
            "axisLabel": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{value} ml"
            },
            "inverse": false,
            "position": "left",
            "offset": 80,
            "splitNumber": 5,
            "min": 0,
            "max": 250,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        },
        {
            "type": "value",
            "name": "\u84b8\u53d1\u91cf",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLine": {
                "show": true,
                "onZero": true,
                "onZeroAxisIndex": 0
            },
            "axisLabel": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{value} ml"
            },
            "inverse": false,
            "position": "left",
            "offset": 0,
            "splitNumber": 5,
            "min": 0,
            "max": 250,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        },
        {
            "type": "value",
            "name": "\u6e29\u5ea6",
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLine": {
                "show": true,
                "onZero": true,
                "onZeroAxisIndex": 0
            },
            "axisLabel": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{value} \u00b0C"
            },
            "inverse": false,
            "position": "right",
            "offset": 0,
            "splitNumber": 5,
            "min": 0,
            "max": 25,
            "minInterval": 0,
            "splitLine": {
                "show": true,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_b5820dae5a0744c4a4ae315d9b2037b0.setOption(option_b5820dae5a0744c4a4ae315d9b2037b0);
    </script>
</body>
</html>





```python
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
    .add_schema(maptype="china")
    .add(
        "",
        [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
        type_=ChartType.EFFECT_SCATTER,
        color="white",
    )
    .add(
        "geo",
        [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="blue"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)
c.set_global_opts(
    title_opts=opts.TitleOpts(title="Geo-Lines", subtitle="副标题"),
    toolbox_opts=opts.ToolboxOpts(
        is_show=True,
        orient="vertical",
        feature=opts.ToolBoxFeatureOpts(
            save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(type_="jpeg", title="保存为jpeg",background_color='white',pixel_ratio=10), # 
            restore=opts.ToolBoxFeatureRestoreOpts(),
            data_view=opts.ToolBoxFeatureDataViewOpts(),
            data_zoom=opts.ToolBoxFeatureDataZoomOpts(),
            magic_type=opts.ToolBoxFeatureDataViewOpts(),
            brush=opts.ToolBoxFeatureDataZoomOpts(),
        )
    )
)
c.render("geo_lines.html")
```




    '/Users/wzf/Desktop/code/shujunge_package/Visualization/my_pyecharts/geo_lines.html'




```python
# # 导入输出图片工具
# from pyecharts.render import make_snapshot
# # 使用snapshot-selenium 渲染图片
# from snapshot_selenium import snapshot

# # 输出保存为图片
# make_snapshot(snapshot, c.render(), "geo.pdf")
```


```python
from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    {"name": "结点1", "symbolSize": 10},
    {"name": "结点2", "symbolSize": 20},
    {"name": "结点3", "symbolSize": 30},
    {"name": "结点4", "symbolSize": 40},
    {"name": "结点5", "symbolSize": 50},
    {"name": "结点6", "symbolSize": 40},
    {"name": "结点7", "symbolSize": 30},
    {"name": "结点8", "symbolSize": 20},
]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="bb5bc643fb8f4f089770d9a77db65624" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_bb5bc643fb8f4f089770d9a77db65624 = echarts.init(
            document.getElementById('bb5bc643fb8f4f089770d9a77db65624'), 'white', {renderer: 'canvas'});
        var option_bb5bc643fb8f4f089770d9a77db65624 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "graph",
            "layout": "force",
            "symbolSize": 10,
            "circular": {
                "rotateLabel": false
            },
            "force": {
                "repulsion": 8000,
                "edgeLength": 50,
                "gravity": 0.2
            },
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "show": true,
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "roam": true,
            "draggable": false,
            "focusNodeAdjacency": true,
            "data": [
                {
                    "name": "\u7ed3\u70b91",
                    "symbolSize": 10
                },
                {
                    "name": "\u7ed3\u70b92",
                    "symbolSize": 20
                },
                {
                    "name": "\u7ed3\u70b93",
                    "symbolSize": 30
                },
                {
                    "name": "\u7ed3\u70b94",
                    "symbolSize": 40
                },
                {
                    "name": "\u7ed3\u70b95",
                    "symbolSize": 50
                },
                {
                    "name": "\u7ed3\u70b96",
                    "symbolSize": 40
                },
                {
                    "name": "\u7ed3\u70b97",
                    "symbolSize": 30
                },
                {
                    "name": "\u7ed3\u70b98",
                    "symbolSize": 20
                }
            ],
            "edgeLabel": {
                "show": false,
                "position": "top",
                "margin": 8
            },
            "edgeSymbol": [
                null,
                null
            ],
            "edgeSymbolSize": 10,
            "links": [
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b98"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b98"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b98"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b98"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b98"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b96",
                    "target": "\u7ed3\u70b98"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b97",
                    "target": "\u7ed3\u70b98"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b91"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b96"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b97"
                },
                {
                    "source": "\u7ed3\u70b98",
                    "target": "\u7ed3\u70b98"
                }
            ]
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "Graph-\u57fa\u672c\u793a\u4f8b",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_bb5bc643fb8f4f089770d9a77db65624.setOption(option_bb5bc643fb8f4f089770d9a77db65624);
    </script>
</body>
</html>





```python
from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    opts.GraphNode(name="结点1", symbol_size=10),
    opts.GraphNode(name="结点2", symbol_size=20),
    opts.GraphNode(name="结点3", symbol_size=30),
    opts.GraphNode(name="结点4", symbol_size=40),
    opts.GraphNode(name="结点5", symbol_size=50),
]
links = [
    opts.GraphLink(source="结点1", target="结点2"),
    opts.GraphLink(source="结点2", target="结点3"),
    opts.GraphLink(source="结点3", target="结点4"),
    opts.GraphLink(source="结点4", target="结点5"),
    opts.GraphLink(source="结点5", target="结点1"),
]
c = (
    Graph()
    .add("", nodes, links, repulsion=4000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink"))
)
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="02b923021d3b4f9aa91f19eab3cb6706" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_02b923021d3b4f9aa91f19eab3cb6706 = echarts.init(
            document.getElementById('02b923021d3b4f9aa91f19eab3cb6706'), 'white', {renderer: 'canvas'});
        var option_02b923021d3b4f9aa91f19eab3cb6706 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "graph",
            "layout": "force",
            "symbolSize": 10,
            "circular": {
                "rotateLabel": false
            },
            "force": {
                "repulsion": 4000,
                "edgeLength": 50,
                "gravity": 0.2
            },
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "show": true,
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "roam": true,
            "draggable": false,
            "focusNodeAdjacency": true,
            "data": [
                {
                    "name": "\u7ed3\u70b91",
                    "fixed": false,
                    "symbolSize": 10
                },
                {
                    "name": "\u7ed3\u70b92",
                    "fixed": false,
                    "symbolSize": 20
                },
                {
                    "name": "\u7ed3\u70b93",
                    "fixed": false,
                    "symbolSize": 30
                },
                {
                    "name": "\u7ed3\u70b94",
                    "fixed": false,
                    "symbolSize": 40
                },
                {
                    "name": "\u7ed3\u70b95",
                    "fixed": false,
                    "symbolSize": 50
                }
            ],
            "edgeLabel": {
                "show": false,
                "position": "top",
                "margin": 8
            },
            "edgeSymbol": [
                null,
                null
            ],
            "edgeSymbolSize": 10,
            "links": [
                {
                    "source": "\u7ed3\u70b91",
                    "target": "\u7ed3\u70b92"
                },
                {
                    "source": "\u7ed3\u70b92",
                    "target": "\u7ed3\u70b93"
                },
                {
                    "source": "\u7ed3\u70b93",
                    "target": "\u7ed3\u70b94"
                },
                {
                    "source": "\u7ed3\u70b94",
                    "target": "\u7ed3\u70b95"
                },
                {
                    "source": "\u7ed3\u70b95",
                    "target": "\u7ed3\u70b91"
                }
            ]
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "Graph-GraphNode-GraphLink",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_02b923021d3b4f9aa91f19eab3cb6706.setOption(option_02b923021d3b4f9aa91f19eab3cb6706);
    </script>
</body>
</html>





```python
import random

from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker


data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
c = (
    Bar3D()
    .add(
        "",
        [[d[1], d[0], d[2]] for d in data],
        xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=20),
        title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
    )
)
c.load_javascript()
c.render_notebook()
```




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
        <div id="66161a33572240c093eaf429bcd7cbf6" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_66161a33572240c093eaf429bcd7cbf6 = echarts.init(
            document.getElementById('66161a33572240c093eaf429bcd7cbf6'), 'white', {renderer: 'canvas'});
        var option_66161a33572240c093eaf429bcd7cbf6 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar3D",
            "data": [
                [
                    0,
                    0,
                    8
                ],
                [
                    1,
                    0,
                    9
                ],
                [
                    2,
                    0,
                    4
                ],
                [
                    3,
                    0,
                    1
                ],
                [
                    4,
                    0,
                    5
                ],
                [
                    5,
                    0,
                    11
                ],
                [
                    6,
                    0,
                    9
                ],
                [
                    7,
                    0,
                    8
                ],
                [
                    8,
                    0,
                    12
                ],
                [
                    9,
                    0,
                    12
                ],
                [
                    10,
                    0,
                    0
                ],
                [
                    11,
                    0,
                    12
                ],
                [
                    12,
                    0,
                    6
                ],
                [
                    13,
                    0,
                    5
                ],
                [
                    14,
                    0,
                    10
                ],
                [
                    15,
                    0,
                    6
                ],
                [
                    16,
                    0,
                    4
                ],
                [
                    17,
                    0,
                    5
                ],
                [
                    18,
                    0,
                    6
                ],
                [
                    19,
                    0,
                    0
                ],
                [
                    20,
                    0,
                    4
                ],
                [
                    21,
                    0,
                    5
                ],
                [
                    22,
                    0,
                    12
                ],
                [
                    23,
                    0,
                    4
                ],
                [
                    0,
                    1,
                    2
                ],
                [
                    1,
                    1,
                    8
                ],
                [
                    2,
                    1,
                    2
                ],
                [
                    3,
                    1,
                    3
                ],
                [
                    4,
                    1,
                    1
                ],
                [
                    5,
                    1,
                    11
                ],
                [
                    6,
                    1,
                    4
                ],
                [
                    7,
                    1,
                    12
                ],
                [
                    8,
                    1,
                    3
                ],
                [
                    9,
                    1,
                    3
                ],
                [
                    10,
                    1,
                    9
                ],
                [
                    11,
                    1,
                    1
                ],
                [
                    12,
                    1,
                    12
                ],
                [
                    13,
                    1,
                    12
                ],
                [
                    14,
                    1,
                    2
                ],
                [
                    15,
                    1,
                    0
                ],
                [
                    16,
                    1,
                    11
                ],
                [
                    17,
                    1,
                    3
                ],
                [
                    18,
                    1,
                    1
                ],
                [
                    19,
                    1,
                    12
                ],
                [
                    20,
                    1,
                    0
                ],
                [
                    21,
                    1,
                    6
                ],
                [
                    22,
                    1,
                    12
                ],
                [
                    23,
                    1,
                    8
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    1,
                    2,
                    7
                ],
                [
                    2,
                    2,
                    10
                ],
                [
                    3,
                    2,
                    3
                ],
                [
                    4,
                    2,
                    1
                ],
                [
                    5,
                    2,
                    5
                ],
                [
                    6,
                    2,
                    12
                ],
                [
                    7,
                    2,
                    11
                ],
                [
                    8,
                    2,
                    11
                ],
                [
                    9,
                    2,
                    5
                ],
                [
                    10,
                    2,
                    7
                ],
                [
                    11,
                    2,
                    5
                ],
                [
                    12,
                    2,
                    2
                ],
                [
                    13,
                    2,
                    7
                ],
                [
                    14,
                    2,
                    11
                ],
                [
                    15,
                    2,
                    10
                ],
                [
                    16,
                    2,
                    9
                ],
                [
                    17,
                    2,
                    4
                ],
                [
                    18,
                    2,
                    2
                ],
                [
                    19,
                    2,
                    0
                ],
                [
                    20,
                    2,
                    9
                ],
                [
                    21,
                    2,
                    2
                ],
                [
                    22,
                    2,
                    5
                ],
                [
                    23,
                    2,
                    11
                ],
                [
                    0,
                    3,
                    12
                ],
                [
                    1,
                    3,
                    1
                ],
                [
                    2,
                    3,
                    4
                ],
                [
                    3,
                    3,
                    7
                ],
                [
                    4,
                    3,
                    10
                ],
                [
                    5,
                    3,
                    5
                ],
                [
                    6,
                    3,
                    0
                ],
                [
                    7,
                    3,
                    4
                ],
                [
                    8,
                    3,
                    6
                ],
                [
                    9,
                    3,
                    7
                ],
                [
                    10,
                    3,
                    6
                ],
                [
                    11,
                    3,
                    11
                ],
                [
                    12,
                    3,
                    2
                ],
                [
                    13,
                    3,
                    7
                ],
                [
                    14,
                    3,
                    5
                ],
                [
                    15,
                    3,
                    8
                ],
                [
                    16,
                    3,
                    3
                ],
                [
                    17,
                    3,
                    9
                ],
                [
                    18,
                    3,
                    9
                ],
                [
                    19,
                    3,
                    10
                ],
                [
                    20,
                    3,
                    11
                ],
                [
                    21,
                    3,
                    11
                ],
                [
                    22,
                    3,
                    1
                ],
                [
                    23,
                    3,
                    8
                ],
                [
                    0,
                    4,
                    9
                ],
                [
                    1,
                    4,
                    4
                ],
                [
                    2,
                    4,
                    6
                ],
                [
                    3,
                    4,
                    12
                ],
                [
                    4,
                    4,
                    12
                ],
                [
                    5,
                    4,
                    9
                ],
                [
                    6,
                    4,
                    7
                ],
                [
                    7,
                    4,
                    2
                ],
                [
                    8,
                    4,
                    2
                ],
                [
                    9,
                    4,
                    5
                ],
                [
                    10,
                    4,
                    3
                ],
                [
                    11,
                    4,
                    6
                ],
                [
                    12,
                    4,
                    5
                ],
                [
                    13,
                    4,
                    8
                ],
                [
                    14,
                    4,
                    8
                ],
                [
                    15,
                    4,
                    9
                ],
                [
                    16,
                    4,
                    8
                ],
                [
                    17,
                    4,
                    4
                ],
                [
                    18,
                    4,
                    6
                ],
                [
                    19,
                    4,
                    1
                ],
                [
                    20,
                    4,
                    9
                ],
                [
                    21,
                    4,
                    5
                ],
                [
                    22,
                    4,
                    9
                ],
                [
                    23,
                    4,
                    6
                ],
                [
                    0,
                    5,
                    3
                ],
                [
                    1,
                    5,
                    9
                ],
                [
                    2,
                    5,
                    2
                ],
                [
                    3,
                    5,
                    11
                ],
                [
                    4,
                    5,
                    8
                ],
                [
                    5,
                    5,
                    12
                ],
                [
                    6,
                    5,
                    12
                ],
                [
                    7,
                    5,
                    11
                ],
                [
                    8,
                    5,
                    5
                ],
                [
                    9,
                    5,
                    11
                ],
                [
                    10,
                    5,
                    7
                ],
                [
                    11,
                    5,
                    1
                ],
                [
                    12,
                    5,
                    12
                ],
                [
                    13,
                    5,
                    1
                ],
                [
                    14,
                    5,
                    0
                ],
                [
                    15,
                    5,
                    5
                ],
                [
                    16,
                    5,
                    0
                ],
                [
                    17,
                    5,
                    9
                ],
                [
                    18,
                    5,
                    10
                ],
                [
                    19,
                    5,
                    12
                ],
                [
                    20,
                    5,
                    11
                ],
                [
                    21,
                    5,
                    4
                ],
                [
                    22,
                    5,
                    12
                ],
                [
                    23,
                    5,
                    9
                ]
            ],
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "visualMap": {
        "show": true,
        "type": "continuous",
        "min": 0,
        "max": 20,
        "inRange": {
            "color": [
                "#50a3ba",
                "#eac763",
                "#d94e5d"
            ]
        },
        "calculable": true,
        "inverse": false,
        "splitNumber": 5,
        "orient": "vertical",
        "showLabel": true,
        "itemWidth": 20,
        "itemHeight": 140,
        "borderWidth": 0
    },
    "xAxis3D": {
        "data": [
            "12a",
            "1a",
            "2a",
            "3a",
            "4a",
            "5a",
            "6a",
            "7a",
            "8a",
            "9a",
            "10a",
            "11a",
            "12p",
            "1p",
            "2p",
            "3p",
            "4p",
            "5p",
            "6p",
            "7p",
            "8p",
            "9p",
            "10p",
            "11p"
        ],
        "nameGap": 20,
        "type": "category",
        "axisLabel": {
            "margin": 8
        }
    },
    "yAxis3D": {
        "data": [
            "Saturday",
            "Friday",
            "Thursday",
            "Wednesday",
            "Tuesday",
            "Monday",
            "Sunday"
        ],
        "nameGap": 20,
        "type": "category",
        "axisLabel": {
            "margin": 8
        }
    },
    "zAxis3D": {
        "nameGap": 20,
        "type": "value",
        "axisLabel": {
            "margin": 8
        }
    },
    "grid3D": {
        "boxWidth": 200,
        "boxHeight": 100,
        "boxDepth": 80,
        "viewControl": {
            "autoRotate": false,
            "autoRotateSpeed": 10,
            "rotateSensitivity": 1
        }
    },
    "title": [
        {
            "text": "Bar3D-\u57fa\u672c\u793a\u4f8b",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_66161a33572240c093eaf429bcd7cbf6.setOption(option_66161a33572240c093eaf429bcd7cbf6);
    </script>
</body>
</html>



