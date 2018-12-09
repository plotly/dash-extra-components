export const timestampProp = (prop_name, value) => {
    const payload = {};
    payload[prop_name] = value;
    payload[`${prop_name}_timestamp`] = new Date();
    return payload;
};
