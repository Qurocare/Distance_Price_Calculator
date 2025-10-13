import streamlit as st

st.set_page_config(page_title="Qurocare Rate Calculator", layout="centered")

st.title("🏥 Qurocare Homecare Service Rate Calculator")
st.write("Select a service and distance to calculate the visit rate.")

# ------------------------------------------------------
# Function to calculate charges
# ------------------------------------------------------
def calculate_charge(service, distance, hlc_type=None):
    if service == "HDC":  # Doctor Consultation
        if distance <= 3:
            return 1599
        elif distance <= 6:
            return 1799
        elif distance <= 8:
            return 1899
        elif distance <= 10:
            return 1999
        else:
            extra_km = distance - 10
            return 1999 + (extra_km * 30)

    elif service == "HNV":  # Home Nurse Visit
        if distance <= 3:
            return 399
        elif distance <= 6:
            return 499
        elif distance <= 8:
            return 549
        elif distance <= 10:
            return 599
        else:
            extra_km = distance - 10
            return 599 + (extra_km * 30)

    elif service == "HPT":  # Home Physiotherapy
        # Returns a dictionary with three price options
        if distance <= 3:
            return {"Single": 1000, "Daily Pay": 900, "Upfront Pay": 850}
        elif distance <= 7:
            return {"Single": 1100, "Daily Pay": 1000, "Upfront Pay": 950}
        elif distance <= 12:
            return {"Single": 1300, "Daily Pay": 1200, "Upfront Pay": 1150}
        else:
            return {"Single": 1500, "Daily Pay": 1400, "Upfront Pay": 1350}

    elif service == "HLC":  # Home Lab Collection
        if hlc_type == "Regular":
            if distance <= 3:
                return 99
            elif distance <= 6:
                return 120
            elif distance <= 8:
                return 150
            elif distance <= 10:
                return 200
            elif distance <= 15:
                extra_km = distance - 10
                return 200 + (extra_km * 30)
            else:
                return "❌ Service not available beyond 15 km"

        elif hlc_type == "Offer":
            if distance <= 8:
                return 0
            elif distance <= 10:
                return 99
            elif distance <= 15:
                extra_km = distance - 10
                return 99 + (extra_km * 30)
            else:
                return "❌ Service not available beyond 15 km"


# ------------------------------------------------------
# User Interface
# ------------------------------------------------------
service = st.selectbox("Select Service Type", ["Select", "HDC", "HNV", "HLC", "HPT"])

if service != "Select":
    # restrict distance to 15 km max for all
    distance = st.slider("Select Distance from Clinic (in km)", 0.0, 15.0, 3.0, 0.5)
    st.caption("🚗 Service available only up to 15 km from clinic")

    if service == "HLC":
        hlc_type = st.radio("Select HLC Category", ["Regular", "Offer"])
        result = calculate_charge(service, distance, hlc_type)
        st.markdown("---")

        st.subheader("🧾 Calculated Rate:")
        if isinstance(result, (int, float)):
            st.success(f"**HLC ({hlc_type})** rate for {distance} km: ₹{result:.2f}")
        else:
            st.error(result)

    elif service == "HPT":
        result = calculate_charge(service, distance)
        st.markdown("---")
        st.subheader(f"HPT (Physiotherapy) Rates for {distance} km:")
        st.write(f"• Single Session: ₹{result['Single']}")
        st.write(f"• Daily Pay (Multiple Days): ₹{result['Daily Pay']}/day")
        st.write(f"• Upfront Pay (Multiple Days): ₹{result['Upfront Pay']}/day")

    else:  # HDC and HNV
        result = calculate_charge(service, distance)
        st.markdown("---")
        st.subheader("Calculated Rate:")
        if distance > 15:
            st.error("❌ Service not available beyond 15 km")
        else:
            st.success(f"{service} service rate for {distance} km: ₹{result:.2f}")

# ------------------------------------------------------
# Footer
# ------------------------------------------------------
st.markdown("---")
st.caption("Developed by Qurocare Team 💚")

