// ==UserScript==
// @name     TDX_Main
// @version  3
// @grant    none
// ==/UserScript==

// https://tdx.umn.edu/TDNext/Home/Desktop/Default.aspx

if (!window.location.pathname.includes("Desktop")){
  console.log("TDX_Main: Not on Desktop");
  return;    
}

var interOFF = true; // Interval OFF - Used to focus on the search box.
// var assets = ""; // Assets to be searched.

var inter = setInterval(function () {
  if (localStorage.getItem("Message") == "On") {
    document.getElementById("dropdownMenu1").innerHTML =
      "<h2><font color='#9900FF'>Press F1 to "
      + (interOFF ? "Enable" : "Disable") +
      " Search Bar Auto Focus</font></h2>";
  }
  if (interOFF) return;

  frame = document.getElementById("assetai_30");
  doc = frame.contentDocument || frame.contentWindow.document;
  box = doc.getElementById("txtAssetSerial");
  if (!box) return;
  if (document.activeElement !== frame || doc.activeElement !== box) {
    box.focus();
    box.setSelectionRange(0, box.value.length);
    box.scrollIntoView(true);
  }

  frame = document.getElementById("assetai_30");
  doc = frame.contentDocument || frame.contentWindow.document;
  doc.removeEventListener("keydown", textBox);
  doc.addEventListener("keydown", textBox);
}, 200);


window.addEventListener('load', (event) => {
  document.getElementById("divTDBar").getElementsByTagName("a")[0].innerText = "Univerity of Minesota";

  if (localStorage.getItem("Message") == "On")
    interOFF = localStorage.getItem("interOFF") == "true" ? true : false;

  tabs = document.getElementById("tabsList").children;
  for (i = 0; i < tabs.length; i++) { //Select the Assets tab.
    if (tabs[i].getElementsByTagName("a")[0].innerText == "Assets/CIs") {
      tabs[i].getElementsByTagName("a")[0].click();
    }
  }

  document.addEventListener("keydown", textBox);
});


function textBox(event) {
  console.log("Main: " + event.which);
  if (event.which == "13") { //Enter
    event.preventDefault();
    frame = document.getElementById("assetai_30");
    doc = frame.contentDocument || frame.contentWindow.document;
    box = doc.getElementById("txtAssetSerial");

    doc.getElementById("btnAssetLookup").click();

    //box.value = "";
    box.focus();
    box.setSelectionRange(0, box.value.length);
    box.scrollIntoView(true);
  }
  if (event.which == "112" || event.which == "113") { //F1 & F2
    event.preventDefault();

    if (event.which == "112") { // F1
      interOFF = !interOFF;
      localStorage.setItem("interOFF", interOFF);
    }

    if (event.which == "113") { // F2
      frame = document.getElementById("assetai_30");
      doc = frame.contentDocument || frame.contentWindow.document;
      val = doc.getElementById("txtAssetSerial").value;
      window = window.open("/TDNext/Apps/30/Assets/New?formId=7&id=" + val, "_blank", "width=1200,height=800");
    }
  }

  if (event.which == "114" || event.which == "115") { //F3 & F4
    event.preventDefault();
  }

  if (event.which == "46") { //Delete
    event.preventDefault();
    // localStorage.setItem("Message", "On");
    localStorage.setItem("Message", localStorage.getItem("Message") == "On" ? "Off" : "On");
  }

  // if (event.which == "123") { //F12
  //     event.preventDefault();

  //     if (event.ctrlKey && event.shiftKey) {
  //         assets = prompt("Enter SNs: ").trim().split(' ');
  //         console.log(assets);
  //     } else {
  //         frame = document.getElementById("assetai_30");
  //         doc = frame.contentDocument || frame.contentWindow.document;
  //         doc.getElementById("txtAssetSerial").value = assets.pop();
  //         doc.getElementById("btnAssetLookup").click();
  //         document.title = assets.length + " Remaining";
  //     }
  // }
}

