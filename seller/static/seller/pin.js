const pincode = document.querySelector('input');
const parentID = document.getElementById('dropdown-menu');
var po_url = "https://api.postalpincode.in/pincode/"
pincode.addEventListener('change', updateValue);

function updateValue(e) {
  po_url+=e.target.value;

  (async () => {
    const res = await fetch(po_url)
      .then(response => response.json())
      .then(responseData =>{const resp = responseData[0];
                            return resp;})
    if (res.Status=="Success") {
      resPOffice = res.PostOffice;
      for (let i = 0; i < res.Message[res.Message.length-1]; i++) {
        var newElement = document.createElement("A");
        newElement.setAttribute('id', "dropdown-item");
        newElement.setAttribute('class', "dropdown-item");
        linkSelected="/accounts/edit/pin/"+resPOffice[i].Name+"-"+resPOffice[i].District+"-"+resPOffice[i].State+"/"+e.target.value
        newElement.setAttribute('href', linkSelected);
        newElement.innerHTML = resPOffice[i].Name+", "+resPOffice[i].District+", "+resPOffice[i].State;
        parentID.appendChild(newElement);
      }
    }
  })();

}

