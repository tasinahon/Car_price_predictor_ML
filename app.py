import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

company = ['Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota',
       'Renault', 'Honda', 'Datsun', 'Tata', 'Volkswagen', 'Chevrolet',
       'BMW', 'Nissan', 'Hindustan', 'Fiat', 'Force', 'Mercedes',
       'Mitsubishi', 'Jeep']

name=['Hyundai Santro Xing XO eRLX Euro III', 'Mahindra Jeep CL550 MDI',
       'Hyundai Grand i10 Magna 1.2 Kappa VTVT',
       'Ford EcoSport Titanium 1.5L TDCi', 'Ford Figo', 'Hyundai Eon',
       'Ford EcoSport Ambiente 1.5L TDCi',
       'Maruti Suzuki Alto K10 VXi AMT', 'Skoda Fabia Classic 1.2 MPI',
       'Maruti Suzuki Stingray VXi', 'Hyundai Elite i20 Magna 1.2',
       'Mahindra Scorpio SLE BS IV', 'Audi Q7', 'Mahindra Scorpio S10',
       'Maruti Suzuki Alto 800', 'Maruti Suzuki Alto 800 Vxi',
       'Hyundai i20 Sportz 1.2', 'Maruti Suzuki Alto 800 Lx',
       'Maruti Suzuki Vitara Brezza ZDi', 'Maruti Suzuki Alto LX',
       'Mahindra Bolero DI', 'Maruti Suzuki Swift Dzire ZDi',
       'Mahindra Scorpio S10 4WD', 'Maruti Suzuki Swift Vdi BSIII',
       'Maruti Suzuki Wagon R VXi BS III',
       'Maruti Suzuki Wagon R VXi Minor',
       'Toyota Innova 2.0 G 8 STR BS IV', 'Renault Lodgy 85 PS RXL',
       'Skoda Yeti Ambition 2.0 TDI CR 4x2',
       'Maruti Suzuki Baleno Delta 1.2',
       'Renault Duster 110 PS RxZ Diesel Plus',
       'Renault Duster 85 PS RxE Diesel', 'Honda City 1.5 S MT',
       'Maruti Suzuki Dzire', 'Honda Amaze', 'Honda Amaze 1.5 SX i DTEC',
       'Honda City', 'Datsun Redi GO S', 'Maruti Suzuki SX4 ZXI MT',
       'Maruti Suzuki Swift VXi 1.2 ABS BS IV', 'Honda City ZX CVT',
       'Maruti Suzuki Wagon R LX BS IV', 'Tata Indigo eCS LS CR4 BS IV',
       'Volkswagen Polo Highline Exquisite P', 'Chevrolet Spark LS 1.0',
       'Renault Duster 110PS Diesel RxZ',
       'Skoda Fabia 1.2L Diesel Ambiente', 'Renault Duster',
       'Mahindra Scorpio S4', 'Mahindra Scorpio VLX 2WD BS IV',
       'Mahindra Quanto C8', 'Ford EcoSport', 'Honda Brio',
       'Hyundai i20 Magna', 'Toyota Corolla Altis Diesel D4DG',
       'Hyundai Verna Transform SX VTVT',
       'Toyota Corolla Altis Petrol Ltd', 'Honda City 1.5 EXi New',
       'Skoda Fabia 1.2L Diesel Elegance', 'BMW 3 Series 320i',
       'Maruti Suzuki A Star Lxi', 'Toyota Etios GD',
       'Ford Figo Diesel EXI Option',
       'Maruti Suzuki Swift Dzire VXi 1.2 BS IV',
       'Chevrolet Beat LT Diesel', 'Mahindra XUV500 W8 AWD 2013',
       'Hyundai i10 Magna 1.2', 'Hyundai Verna Fluidic New',
       'Maruti Suzuki Swift VXi 1.2 BS IV',
       'Maruti Suzuki Ertiga ZXI Plus', 'Maruti Suzuki Ertiga Vxi',
       'Maruti Suzuki Ertiga VDi', 'Maruti Suzuki Alto LXi BS III',
       'Hyundai Grand i10 Asta 1.1 CRDi', 'Honda Amaze 1.2 S i VTEC',
       'Hyundai i20 Asta 1.4 CRDI 6 Speed', 'Ford Figo Diesel EXI',
       'Maruti Suzuki Eeco 5 STR WITH AC HTR', 'Maruti Suzuki Ertiga ZXi',
       'Maruti Suzuki Esteem LXi BS III', 'Maruti Suzuki Ritz VXI',
       'Maruti Suzuki Ritz LDi', 'Maruti Suzuki Dzire VDI',
       'Toyota Etios Liva G', 'Hyundai i20 Sportz 1.4 CRDI',
       'Chevrolet Spark', 'Nissan Micra XV', 'Maruti Suzuki Swift',
       'Honda Amaze 1.5 S i DTEC', 'Chevrolet Beat', 'Toyota Corolla',
       'Honda City 1.5 V MT', 'Ford EcoSport Trend 1.5L TDCi',
       'Hyundai i20 Asta 1.2', 'Tata Indica V2 eLS',
       'Hindustan Motors Ambassador', 'Toyota Corolla Altis 1.8 GL',
       'Toyota Corolla Altis 1.8 J', 'Toyota Innova 2.5 GX BS IV 7 STR',
       'Volkswagen Jetta Highline TDI AT',
       'Volkswagen Polo Comfortline 1.2L P', 'Volkswagen Polo',
       'Nissan Sunny', 'Hyundai Elite i20', 'Renault Kwid',
       'Mahindra Scorpio VLX Airbag', 'Maruti Suzuki Alto 800 Lxi',
       'Chevrolet Spark LT 1.0', 'Datsun Redi GO T O',
       'Maruti Suzuki Swift RS VDI', 'Fiat Punto Emotion 1.2',
       'Hyundai i10 Sportz 1.2', 'Chevrolet Beat LT Opt Diesel',
       'Chevrolet Beat LS Diesel', 'Tata Indigo CS',
       'Maruti Suzuki Swift VDi', 'Hyundai Eon Era Plus',
       'Mahindra XUV500', 'Ford Fiesta', 'Maruti Suzuki Wagon R',
       'Hyundai i20', 'Tata Indigo eCS LX TDI BS III',
       'Hyundai Fluidic Verna 1.6 CRDi SX', 'Fiat Petra ELX 1.2 PS',
       'Hyundai Santro Xing XS', 'Maruti Suzuki Ciaz VXi Plus',
       'Maruti Suzuki Zen VX', 'Hyundai Creta 1.6 SX Plus Petrol',
       'Mahindra Scorpio SLX', 'Toyota Innova 2.5 G BS III 8 STR',
       'Maruti Suzuki Wagon R LXI BS IV', 'Tata Nano Cx BSIV',
       'Maruti Suzuki Alto Std BS IV', 'Maruti Suzuki Wagon R LXi BS III',
       'Maruti Suzuki Swift VXI BSIII',
       'Tata Sumo Victa EX 10 by 7 Str BSIII',
       'Volkswagen Passat Diesel Comfortline AT',
       'Renault Scala RxL Diesel Travelogue',
       'Hyundai Grand i10 Sportz O 1.2 Kappa VTVT',
       'Hyundai i20 Active 1.2 SX', 'Mahindra Xylo E4',
       'Mahindra Jeep MM 550 XDB', 'Mahindra Bolero SLE BS IV',
       'Force Motors Force One LX ABS 7 STR', 'Maruti Suzuki SX4',
       'Toyota Etios', 'Honda City ZX VTEC',
       'Maruti Suzuki Wagon R LX BS III', 'Honda City VX O MT Diesel',
       'Mahindra Thar CRDe 4x4 AC',
       'Audi A4 1.8 TFSI Multitronic Premium Plus', 'Renault Kwid RXT',
       'Tata Aria Pleasure 4X2', 'Datsun GO T O', 'Honda Jazz VX MT',
       'Hyundai i20 Active 1.4L SX O', 'Maruti Suzuki Ciaz ZXI Plus',
       'Chevrolet Tavera Neo', 'Hyundai Eon Sportz',
       'Tata Sumo Gold Select Variant', 'Maruti Suzuki Wagon R 1.0',
       'Maruti Suzuki Esteem VXi BS III', 'Chevrolet Enjoy 1.4 LS 8 STR',
       'Maruti Suzuki Wagon R 1.0 VXi', 'Nissan Terrano XL D Plus',
       'Renault Duster 85 PS RxL Diesel', 'Maruti Suzuki Dzire ZXI',
       'Renault Kwid RXT Opt', 'Maruti Suzuki Maruti 800 Std',
       'Renault Kwid 1.0 RXT AMT', 'Renault Scala RxL Diesel',
       'Hyundai Grand i10 Asta 1.2 Kappa VTVT O',
       'Chevrolet Beat LS Petrol', 'Hyundai Accent GLX',
       'Mahindra TUV300 T4 Plus', 'Tata Indica V2 Xeta e GLE',
       'Tata Indigo CS LS DiCOR',
       'Mahindra Scorpio VLX Special Edition BS III', 'Honda Accord',
       'Ford EcoSport Titanium 1.5 TDCi', 'Maruti Suzuki Ertiga',
       'Mahindra Scorpio 2.6 CRDe', 'Honda Mobilio',
       'Toyota Corolla Altis', 'Skoda Laura', 'Hyundai Verna Fluidic',
       'Maruti Suzuki Vitara Brezza', 'Mahindra Scorpio',
       'Tata Manza Aura Quadrajet', 'Chevrolet Sail UVA Petrol LT ABS',
       'Hyundai Verna Fluidic 1.6 VTVT SX', 'Hyundai Elantra SX',
       'Mahindra Scorpio VLX 4WD Airbag', 'Mahindra KUV100 K8 D 6 STR',
       'Hyundai Grand i10', 'Hyundai i10', 'Hyundai i20 Active',
       'Datsun Redi GO', 'Toyota Etios Liva', 'Hyundai Accent',
       'Hyundai Verna', 'Hyundai i10 Sportz',
       'Mahindra Bolero Power Plus SLE', 'Honda City 1.5 V MT Exclusive',
       'Chevrolet Spark LT 1.0 Airbag', 'Tata Indigo eCS VX CR4 BS IV',
       'Skoda Rapid Elegance 1.6 TDI CR MT', 'Tata Vista Quadrajet VX',
       'Maruti Suzuki Alto K10 VXi AT', 'Maruti Suzuki Zen LXi BS III',
       'Maruti Suzuki Swift Dzire Tour LDi', 'Honda City ZX EXi',
       'Chevrolet Beat Diesel', 'Hyundai Verna 1.4 VTVT',
       'Toyota Innova 2.5 E MS 7 STR BS IV',
       'Maruti Suzuki Maruti 800 Std – Befo',
       'Hyundai Elite i20 Asta 1.4 CRDI',
       'Maruti Suzuki Versa DX2 8 SEATER BSIII',
       'Tata Indigo LX TDI BS III',
       'Volkswagen Vento Konekt Diesel Highline',
       'Mercedes Benz C Class 200 CDI Classic', 'Hyundai Santro Xing GLS',
       'Maruti Suzuki Omni Limited Edition',
       'Hyundai Sonata Transform 2.4 GDi MT',
       'Hyundai Elite i20 Sportz 1.2', 'Honda Jazz S MT',
       'Hyundai Grand i10 Sportz 1.2 Kappa VTVT',
       'Maruti Suzuki Zen LXi BSII',
       'Mahindra Scorpio W Turbo 2.6DX 9 Seater',
       'Maruti Suzuki Alto K10 VXi',
       'Hyundai Grand i10 Asta 1.2 Kappa VTVT', 'Mahindra XUV500 W8',
       'Hyundai i20 Magna O 1.2', 'Renault Duster 85 PS RxL Explore LE',
       'Honda Brio V MT', 'Ford Ikon 1.3 CLXi NXt Finesse',
       'Toyota Fortuner 3.0 4x4 MT', 'Tata Manza ELAN Quadrajet',
       'Tata Indigo LS', 'Hyundai i20 Magna 1.2',
       'Volkswagen Vento Highline Plus 1.5 Diesel AT',
       'Honda Amaze 1.5 E i DTEC', 'Hyundai Verna 1.6 EX VTVT',
       'Skoda Superb 1.8 TFSI AT', 'Mahindra Bolero DI BSII',
       'Ford Figo Duratorq Diesel Titanium 1.4',
       'Maruti Suzuki Wagon R VXI BS IV', 'Mahindra Logan Diesel 1.5 DLS',
       'Tata Nano GenX XMA', 'Honda City SV', 'Ford Figo Petrol LXI',
       'Hyundai i10 Magna 1.2 Kappa2', 'Toyota Corolla H2',
       'Maruti Suzuki Swift Dzire Tour VXi', 'Tata Indigo CS eLS BS IV',
       'Hyundai Xcent Base 1.1 CRDi', 'Hyundai Accent Executive Edition',
       'Tata Zest XE 75 PS Diesel', 'Maruti Suzuki Dzire LDI',
       'Tata Sumo Gold LX BS IV', 'Toyota Corolla Altis GL Petrol',
       'Maruti Suzuki Eeco 7 STR', 'Mahindra XUV500 W6',
       'Tata Tigor Revotron XZ', 'Maruti Suzuki 800',
       'Honda Mobilio S i DTEC', 'Hyundai Verna 1.6 CRDI E',
       'Maruti Suzuki Omni Select Variant', 'Tata Indica',
       'Hyundai Santro Xing', 'Maruti Suzuki Zen Estilo',
       'Honda Brio VX AT', 'Maruti Suzuki Zen Estilo LXI Green CNG',
       'Maruti Suzuki Wagon R Select Variant', 'Tata Nano Lx BSIV',
       'Hyundai Eon Magna Plus', 'Maruti Suzuki Ritz GENUS VXI',
       'Hyundai Grand i10 Magna AT 1.2 Kappa VTVT',
       'Hyundai Eon D Lite Plus', 'Honda Amaze 1.2 VX i VTEC',
       'Maruti Suzuki Estilo VXi ABS BS IV',
       'Maruti Suzuki Vitara Brezza LDi O', 'Mahindra Scorpio Vlx BSIV',
       'Mitsubishi Lancer 1.8 LXi', 'Maruti Suzuki Maruti 800 AC',
       'Maruti Suzuki Alto 800 LXI CNG O', 'Ford Fiesta SXi 1.6 ABS',
       'Maruti Suzuki Ritz VDi', 'Maruti Suzuki Estilo LX BS IV',
       'Maruti Suzuki Alto', 'Maruti Suzuki Baleno Sigma 1.2',
       'Hyundai Verna 1.6 SX VTVT AT', 'Maruti Suzuki Swift GLAM',
       'Hyundai Getz Prime 1.3 GVS', 'Hyundai Santro',
       'Hyundai Getz Prime 1.3 GLX', 'Chevrolet Beat PS Diesel',
       'Ford EcoSport Trend 1.5 Ti VCT', 'Tata Indica V2 DLG',
       'Honda City 1.5 V AT', 'Tata Nano', 'Chevrolet Cruze LTZ AT',
       'Maruti Suzuki Swift Dzire VDi', 'Maruti Suzuki Alto K10 LXi CNG',
       'Hyundai Accent GLE', 'Force Motors One SUV',
       'Chevrolet Spark 1.0 LT', 'Toyota Etios Liva GD',
       'Renault Duster 85PS Diesel RxL Optional with Nav',
       'Chevrolet Enjoy', 'BMW 5 Series 530i', 'Chevrolet Cruze LTZ',
       'Jeep Wrangler Unlimited 4x4 Diesel',
       'Hyundai Verna VGT CRDi SX ABS', 'Maruti Suzuki Omni',
       'Maruti Suzuki Celerio VDi', 'Tata Zest Quadrajet 1.3',
       'Tata Indigo CS eLX BS IV', 'Hyundai i10 Era',
       'Tata Indigo eCS LX CR4 BS IV', 'Tata Indigo Marina LS',
       'Hyundai Xcent SX 1.2', 'Tata Nano LX Special Edition',
       'Renault Duster 110 PS RxZ Diesel',
       'Maruti Suzuki Wagon R AX BSIV', 'Maruti Suzuki Alto K10 New',
       'Mahindra Xylo E8', 'Tata Manza Aqua Quadrajet',
       'Renault Kwid 1.0', 'Tata Venture EX 8 STR',
       'Maruti Suzuki Swift Dzire Tour LXi',
       'Skoda Octavia Classic 1.9 TDI MT', 'Maruti Suzuki Omni LPG BS IV',
       'Tata Sumo Gold EX BS IV', 'Hyundai Verna 1.6 CRDI SX',
       'Mahindra Scorpio SLX 2.6 Turbo 8 Str', 'Ford Ikon 1.6 Nxt',
       'Toyota Innova 2.5 V 7 STR', 'Nissan Sunny XL',
       'Maruti Suzuki Swift VDi BS IV', 'Toyota Innova 2.0 G4',
       'Maruti Suzuki Swift VDi ABS', 'Hyundai Elite i20 Asta 1.2',
       'Volkswagen Polo Trendline 1.5L D', 'Toyota Etios Liva Diesel',
       'Maruti Suzuki Ciaz ZXi Plus RS', 'Hyundai Elantra 1.8 S',
       'Ford EcoSport Trend 1.5L Ti VCT', 'Tata Indica eV2 LS',
       'Maruti Suzuki Swift ZXi 1.2 BS IV',
       'Maruti Suzuki S Cross Sigma 1.3', 'Maruti Suzuki Ertiga LDi',
       'Volkswagen Vento Comfortline Petrol', 'Mahindra KUV100',
       'Maruti Suzuki Swift Dzire Tour VDi', 'Mahindra Scorpio 2.6 SLX',
       'Maruti Suzuki Omni 8 STR BS III',
       'Volkswagen Jetta Comfortline 1.9 TDI AT',
       'Toyota Corolla Altis VL AT Petrol', 'Chevrolet Beat LT Petrol',
       'Volkswagen Vento Comfortline Diesel', 'Tata Indigo CS GLS',
       'Ford Figo Petrol Titanium', 'Honda City ZX GXi',
       'Maruti Suzuki Wagon R Duo Lxi', 'Maruti Suzuki Zen LX BSII',
       'Renault Duster RxL Petrol', 'Maruti Suzuki Baleno Zeta 1.2',
       'Honda WR V S MT Petrol', 'Renault Duster 110 PS RxL Diesel',
       'Mahindra Scorpio LX BS III', 'Hyundai Santro AE GLS Audio',
       'Mahindra Xylo D2 BS IV', 'Hyundai Getz GLE',
       'Hyundai Santro Xing XL AT eRLX Euro III',
       'Hyundai Santro Xing XL eRLX Euro III',
       'Tata Indica V2 DLS BS III', 'Honda City 1.5 E MT',
       'Nissan Micra XL', 'Honda City 1.5 S Inspire',
       'Tata Indica eV2 eXeta eGLX', 'Maruti Suzuki Omni E 8 STR BS IV',
       'Maruti Suzuki Swift LDi', 'Hyundai Verna 1.6 CRDI SX Plus AT',
       'Chevrolet Tavera LS B3 10 Seats BSII', 'Tata Tiago Revotron XM',
       'Tata Tiago Revotorq XZ',
       'Hindustan Motors Ambassador Classic Mark 4 – Befo',
       'Ford Fusion 1.4 TDCi Diesel',
       'Fiat Linea Emotion 1.4 L T Jet Petrol',
       'Ford Ikon 1.3 Flair Josh 100', 'Tata Indica V2 LS',
       'Mahindra Xylo D2', 'Hyundai Eon Magna',
       'Tata Sumo Grande MKII GX', 'Volkswagen Polo Highline1.2L P',
       'Tata Tiago Revotron XZ', 'Tata Indigo eCS',
       'Mahindra Xylo E8 BS IV', 'Tata Sumo Gold FX BSIII',
       'Hyundai Creta', 'Tata Bolt XM Petrol', 'Maruti Suzuki Ritz',
       'Hyundai i20 Asta', 'Maruti Suzuki Swift Select Variant',
       'Tata Indica V2 DLX BS III',
       'Mahindra Scorpio VLX 2.2 mHawk Airbag BSIV',
       'Toyota Innova 2.5 E 8 STR', 'Mahindra KUV100 K8 6 STR',
       'Datsun Go Plus', 'Tata Indica V2', 'Hyundai Santro Xing GL',
       'Toyota Innova 2.5 Z Diesel 7 Seater', 'Maruti Suzuki Alto AX',
       'Mahindra Logan', 'Maruti Suzuki 800 Std BS III',
       'Chevrolet Sail 1.2 LS', 'Tata Manza', 'Toyota Etios G',
       'Toyota Qualis', 'Mahindra Quanto C4', 'Maruti Suzuki Swift Dzire',
       'Hyundai i20 Select Variant', 'Honda City VX Petrol',
       'Hyundai Getz', 'Mercedes Benz C Class 200 K MT', 'Skoda Fabia',
       'Maruti Suzuki Ritz VXI ABS', 'Tata Indica V2 DLE BS III',
       'Tata Zest XM Diesel']

year=[2007, 2006, 2014, 2012, 2013, 2016, 2015, 2010, 2017, 2008, 2018,
       2011, 2009, 2005, 2000, 2019, 2003, 2004, 1995, 2002, 2001]
fuel=['Diesel', 'Petrol', 'LPG']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title("This app tells you the price of car you want to sell.Try it")

s_company = st.selectbox('Select Company Name',sorted(company))
s_model = st.selectbox('Select Car Model',sorted(name))



col1,col2= st.columns(2)

with col1:
    s_year = st.selectbox('Select Purchase year',sorted(year))
with col2:
    s_fuel = st.selectbox('Select Fuel type',sorted(fuel))

kms= st.number_input('Kms_speed')


if st.button('Predict Price'):
    input_df = pd.DataFrame({
        'name': [s_model],
        'company': [s_company],
        'year': [s_year],
        'kms_driven': [kms],
        'fuel_type': [s_fuel]
    })

    
    try:
        result = pipe.predict(input_df)
        st.header("Price: " + str(round(result[0], 2)))
    except Exception as e:
        st.error(f"An error occurred: {e}")
    