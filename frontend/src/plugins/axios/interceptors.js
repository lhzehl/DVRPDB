// lhzehl-blog-t
function setHeaders(config) {
    const headers = config.headers || {};
    config.headers = Object.assign(headers, {
      Authorization: localStorage.getItem("lhzehl-blog-t")
        ? `Token ${localStorage.getItem("lhzehl-blog-t")}`
        : "",
  
      "Content-Type":'multipart/form-data; boundary=----WebKitFormBoundaryBfpW7JErqslMoB7r' 
    });
    return config;
  }
  function returnData(res) {
    return res;
  }
  export default function(axios) {
    axios.interceptors.request.use(setHeaders);
  
    //
    axios.interceptors.response.use(returnData);
  }