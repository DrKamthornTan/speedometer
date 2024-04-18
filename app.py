import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def gauge(gVal, gTitle="", gMode='gauge+number', gSize="FULL", gTheme="Black",
          grLow=.29, grMid=.69, gcLow='#FF1708', gcMid='#FF9400', 
          gcHigh='#1B8720', xpLeft=0, xpRight=1, ypBot=0, ypTop=1, 
          arBot=None, arTop=1, pTheme="streamlit", cWidth=True, sFix=None):

    if sFix == "%":

        gaugeVal = round((gVal * 100), 1)
        top_axis_range = (arTop * 100)
        bottom_axis_range = arBot
        low_gauge_range = (grLow * 100)
        mid_gauge_range = (grMid * 100)

    else:

        gaugeVal = gVal
        top_axis_range = arTop
        bottom_axis_range = arBot
        low_gauge_range = grLow
        mid_gauge_range = grMid

    if gSize == "SML":
        x1, x2, y1, y2 =.25, .25, .75, 1
    elif gSize == "MED":
        x1, x2, y1, y2 = .50, .50, .50, 1
    elif gSize == "LRG":
        x1, x2, y1, y2 = .75, .75, .25, 1
    elif gSize == "FULL":
        x1, x2, y1, y2 = 0, 1, 0, 1
    elif gSize == "CUST":
        x1, x2, y1, y2 = xpLeft, xpRight, ypBot, ypTop   

    if gaugeVal <= low_gauge_range: 
        gaugeColor = gcLow
    elif gaugeVal >= low_gauge_range and gaugeVal <= mid_gauge_range:
        gaugeColor = gcMid
    else:
        gaugeColor = gcHigh

    fig1 = go.Figure(go.Indicator(
        mode = gMode,
        value = gaugeVal,
        domain = {'x': [x1, x2], 'y': [y1, y2]},
        number = {"suffix": sFix},
        title = {'text': gTitle},
        gauge = {
            'axis': {'range': [bottom_axis_range, top_axis_range]},
            'bar' : {'color': gaugeColor}
        }
    ))

    config = {'displayModeBar': False}
    fig1.update_traces(title_font_color=gTheme, selector=dict(type='indicator'))
    fig1.update_traces(number_font_color=gTheme, selector=dict(type='indicator'))
    fig1.update_traces(gauge_axis_tickfont_color=gTheme, selector=dict(type='indicator'))
    fig1.update_layout(margin_b=5)
    fig1.update_layout(margin_l=20)
    fig1.update_layout(margin_r=20)
    fig1.update_layout(margin_t=50)

    fig1.update_layout(margin_autoexpand=True)

    st.plotly_chart(
        fig1, 
        use_container_width=cWidth, 
        theme=pTheme, 
        **{'config':config}
    )

# Create a Streamlit app
def main():
    # Set Streamlit page title
    st.set_page_config(page_title="Gauge Chart Example")
    st.title("DHV AI Startup Speedometer Demo")

    # User input for gauge value
    gauge_value = st.number_input("โปรดใส่ค่าตัวเลข", min_value=0.0, max_value=1.0, step=0.01, value=0.5)

    # Set gauge value
    #gauge_value = 0.1

    # Call the gauge function to create the gauge chart
    gauge(gauge_value, gTitle="")
    

# Run the Streamlit app
if __name__ == "__main__":
    main()