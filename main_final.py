import streamlit as st
import numpy as np
import pandas as pd
import pickle
import altair as alt
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import base64
warnings.filterwarnings('ignore')


def predict_elasticity(df,model_name):
    df=df.iloc[:1,:]
    x=df.values.tolist()
    model=pickle.load(open(model_name,'rb'))
    prediction=model.predict(x)
    return prediction

def func(store,price_range,file_,model_name):
        df_test = pd.read_csv('decaff_160_tetley.csv')
        if store == 'ASDA':
            df_test= df_test[df_test['Retailer Name__ASDA']==True]
        else:
            df_test= df_test[df_test['Retailer Name__ASDA']==False]

        df_test=df_test[['WeekNum_','unit_sales_Tetley_160_Decaff','unit_price_Tetley_160_Decaff']]
        df_test = df_test.iloc[-7:]
        df_test['WeekNum_'].replace(7,"T-6",inplace=True)
        df_test['WeekNum_'].replace(8,"T-5",inplace=True)
        df_test['WeekNum_'].replace(9,"T-4",inplace=True)
        df_test['WeekNum_'].replace(10,"T-3",inplace=True)
        df_test['WeekNum_'].replace(11,"T-2",inplace=True)
        df_test['WeekNum_'].replace(12,"T-1",inplace=True)
        df_test['WeekNum_'].replace(13,"T",inplace=True)
        df_test_ = pd.read_csv(file_)
        df_test_=df_test_.iloc[:,1:]
        
        if store == 'ASDA':
            store = 1.0
        else:
            store = 0.0
        df_test_['Retailer']= store
        df_test_['unit_price_sku']= price_range
        df_test_= df_test_[['unit_price_sku','Retailer', 'Product_1_price_lagged','Product_1_sales_lagged','Product_2_price_lagged','Product_2_sales_lagged','Product_3_price_lagged','Product_3_sales_lagged','Product_4_price_lagged','Product_4_sales_lagged','Product_5_price_lagged', 'Product_5_sales_lagged','Product_6_price_lagged','Product_6_sales_lagged','Product_7_price_lagged','Product_7_sales_lagged','Product_8_price_lagged','Product_8_sales_lagged']]
            #st.write(df_test)
            
        prediction = predict_elasticity(df_test_,model_name)
        new_row = pd.DataFrame({"WeekNum_":"T+1","unit_sales_Tetley_160_Decaff":prediction,"unit_price_Tetley_160_Decaff":price_range})
        df_test = pd.concat([df_test, new_row], ignore_index=True)
        df_test.reset_index(inplace=True)
        chart_data = pd.DataFrame(df_test)
        df_test_revenue= df_test
        df_test_revenue['unit_sales_Tetley_160_Decaff'] = df_test_revenue['unit_sales_Tetley_160_Decaff']*df_test_revenue["unit_price_Tetley_160_Decaff"]
        chart_data_revenue= pd.DataFrame(df_test_revenue)
        
        
        
        choose_graph = st.radio('', ['Sales', 'Revenue'], index = 0)
        
        if choose_graph == 'Sales':
            fig = plt.figure(figsize=(10, 4))
            plt.xlabel("Week")
            plt.ylabel("Sales in Unit")
       
            sns.lineplot(x = "WeekNum_", y = "unit_sales_Tetley_160_Decaff", data = chart_data,marker='o',label='Weekly Unit Sales')
            st.pyplot(fig)
            
        else:
            fig = plt.figure(figsize=(10, 4))
            plt.xlabel("Week")
            plt.ylabel("Revenue")
            sns.lineplot(x = "WeekNum_", y = "unit_sales_Tetley_160_Decaff", data = chart_data_revenue,marker='o',label='Weekly Revenue')
            st.pyplot(fig)
            


def main():
   
    st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 350px !important; # Set the width to your desired value
            background-color:##043c8c;
        }
        .st-emotion-cache-ue6h4q {
            font-size: 14px;
            color: rgb(49, 51, 63);
            display: flex;
            visibility: visible;
            margin-bottom: 0.25rem;
            height: auto;
            margin-top: -10px;
            min-height: 1.5rem;
            vertical-align: middle;
            flex-direction: row;
            -webkit-box-align: center;
            align-items: center;
        }

        # img, svg {
        # height: 100px;
        # width: 100px;
        # border-radius: 2px;
        # }


.st-dk {
    border-top-color: white;
}

.st-dj {
    border-right-color: white;
}

.st-di {
    border-left-color: white;
}
.st-dl {
    border-bottom-color: white;

.st-by {
    background-color: white;
}
}
        .st-d8 {
            cursor: pointer;
            margin-left: 10px;
        }
        .st-emotion-cache-13ejsyy {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 38.4px;
    margin: 0px;
    line-height: 1.6;
    color: white;
    width: auto;
    user-select: none;
    background-color: white;
    border: 1px solid rgba(49, 51, 63, 0.2);
    margin-left: 130px;
    margin-top: -40px;
}
button:not(:disabled) {
    cursor: pointer;
    color: darkblue;
    font-weight: bold;
    border-bottom-color: darkblue;
    border: 5px solid darkblue;
}
.st-emotion-cache-1aehpvj {
    color: rgba(49, 51, 63, 0.6);
    font-size: 1px;
    line-height: 1.25;
}
.st-emotion-cache-16idsys p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 13px;
    color: white;
    font-family: sans-serif;
}
.st-emotion-cache-1inwz65 {
    line-height: 1.6;
    font-weight: normal;
    font-size: 14px;
    font-family: "Source Code Pro", monospace;
    color: white;
}

.st-emotion-cache-1v7f65g .e1b2p2ww6 {
    width: 100%;
    color: white;
}

.st-emotion-cache-10oheav {
    padding: 1rem 0.5rem;
}
.st-emotion-cache-1nm2qww {
    position: absolute;
    top: 0.375rem;
    right: 0.25rem;
    z-index: 1;
    visibility: hidden;
}
.st-emotion-cache-1kzf7z {
    width: 335px;
    position: relative;
    display: flex;
    flex: 1 1 0%;
    flex-direction: column;
    gap: 1rem;
    margin-top: -49px;
    }

.st-emotion-cache-1v7f65g .e1b2p2ww15 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 332px;
}
p, ol, ul, dl {
    margin: 0px 0px 1rem;
    padding: 0px;
    font-size: 1rem;
    font-weight: bold;
    color: darkblue;

}
.st-emotion-cache-76eugy {
    position: relative;
    width: 334px;
    margin-top: -40px;
}
.st-emotion-cache-1ln614r {
    width: 328px;
    position: relative;
    margin-top: -20px;
}

.st-emotion-cache-taue2i {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    padding: 1rem;
    background-color: rgb(255, 255, 255);
    border-radius: 0.5rem;
    color: rgb(49, 51, 63);
    font-size: 12px;
}
  .st-emotion-cache-1vzeuhh {
    -webkit-box-align: center;
    align-items: center;
    background-color: white;
    border-radius: 100%;
    border-style: none;
    box-shadow: none;
    display: flex;
    height: 0.75rem;
    -webkit-box-pack: center;
    justify-content: center;
    width: 0.75rem;
}

.st-by {
    background-color: white;
}

.st-bx {
    border-bottom-color: white;
}

.st-bw {
    border-top-color: white;
}

.st-bv {
    border-right-color: white;
}

.st-bu {
    border-left-color: white;
}



.st-emotion-cache-10y5sf6 {
    font-family: "Source Code Pro", monospace;
    font-size: 14px;
    padding-bottom: 9.33333px;
    color: white;
    top: -22px;
    position: absolute;
    white-space: nowrap;
    background-color: transparent;
    line-height: 1.6;
    font-weight: normal;
}
.st-emotion-cache-hvrj08 {
    width: 310px;
    position: relative;
    margin-top: 6px;
}

.st-emotion-cache-6qob1r {
    position: relative;
    height: 100%;
    width: 100%;
    overflow: overlay;
    background-color: midnightblue;
}

.st-emotion-cache-10trblm {
    position: relative;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    margin-top:15px;
}
#div1
{
    background-color: rgb(4, 60, 140);
    margin-top: -70px;
    height: 80px;
    color: white;
    position:relative;
    width:700px;

}

.st-emotion-cache-cjtidi {
    position: relative;
    width: 355px;
    margin-top: -45px;
}
.st-emotion-cache-1dx1gwv {
    padding: 0px 0px 0px;
    -webkit-box-pack: justify;
    justify-content: space-between;
    -webkit-box-align: center;
    align-items: center;
    # display: flex;
    margin-top: -1px
    </style>
    """,
    unsafe_allow_html=True,
    )
        
    # with st.sidebar:
    #     html_temp = """
    #     <div ">
    #     </div>
    #     """
        # st.markdown(html_temp, unsafe_allow_html=True)

    image = Image.open('logoo.jpg')
    st.sidebar.image(image)
    market = st.sidebar.selectbox('Select Market',('UK','India'))
    sku = st.sidebar.selectbox('Select SKU',('SKU_160_Decaff','SKU_80_Caff'))
    
    store = st.sidebar.selectbox(
    "Select Store",
    ("ASDA","TESCO")
    )
    if sku=='SKU_160_Decaff':

        model_name = './model_5_GB_Tetley_160_Decaff.pkl'

    else:

        model_name = './model_5_GB_Tetley_80_Decaff.pkl'

    price_range = st.sidebar.slider('Select Price', 1.0,5.0,0.1)
    # price_range_text = st.sidebar.text_input('','Type the Price')
    file_ = st.sidebar.file_uploader("Select Model Parameters",type={"csv"})
    predict= st.sidebar.button("Predict")

    html_temp="""<div id="div1">
    <h3 style="color:white; position:relative; margin-left:230px;">Cross Price Elasticity </h3>
     </div> """
    st.markdown(html_temp, unsafe_allow_html=True)
    if st.session_state.get('button') != True:
        st.session_state['button'] = predict
    if st.session_state['button'] == True:
        func(store,price_range,file_,model_name)
            
    
    
        
        

if __name__=='__main__':
    main()