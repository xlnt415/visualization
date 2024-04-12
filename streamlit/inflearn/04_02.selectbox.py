import streamlit as st

def main():
    st.title("커피 주문 키오스크")
    coffee_type = st.selectbox("커피 종류", ["아메리카노", "카페라떼", "카페모카"])

    size = st.radio("사이트", ["Small", "Tall", "Grande"])

    toppings = st.multiselect("토핑", ["시럽", "우유", "초코소스"])

    if st.button("주문하기"):
        st.write("주문이 완료되었습니다!")
        st.write("커피 종류:", coffee_type)
        st.write("사이즈:", size)
        st.write("토핑:", toppings)

if __name__ == '__main__':
    main()