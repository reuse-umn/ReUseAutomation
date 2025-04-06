// ==UserScript==
// @name     TDX_Edit
// @version  4
// @grant    none
// ==/UserScript==

if (!window.location.pathname.includes("Assets")) {
    console.log("TDX_Edit: Not on Assets");
    return;
}

var toST = 0;


class Fields {
    constructor() {
        this.ID_map = new Map([
            // Input
            ["Service Tag", 503],
            ["Serial Number", 502],
            ["Name", 1390],
            ["Comments", 2686],
            ["HDD/SSD Serial Number", 5747],
            ["Owner", 514],
            // Select
            ["State", 2705],
            ["Substate", 2706],
            ["Location", 507],
            ["Location Room", 508],
            ["Use Type", 2697],
        ]);
        this.form_groups = document.getElementsByClassName("form-group");
        this.queue = []
    }

    get_textarea_element(field_name) {
        let field_id = this.ID_map.get(field_name);
        for (let i = 0; i < this.form_groups.length; i++)
            if (this.form_groups[i].getAttribute("data-fieldid") == field_id)
                return this.form_groups[i].getElementsByTagName("textarea")[0]
    }

    find_input(element) {
        let inputs = element.getElementsByTagName("input")
        // REGEX to match only the word attribute and ignore the numbers: attribute####
        for (let j = 0; j < inputs.length; j++)
            if (/attribute[0-9]*/g.test(inputs[j].id))
                return inputs[j];
    }

    set_input(field_name, value, text = null) {
        let field_id = this.ID_map.get(field_name);
        for (let i = 0; i < this.form_groups.length; i++) {
            if (this.form_groups[i].getAttribute("data-fieldid") == field_id) {
                this.form_groups[i].getElementsByTagName("label")[0].innerHTML =
                    "<b>Modified: " + text ? text : value + "</b>";
                return this.find_input(this.form_groups[i]).value = value;
            }
        }
    }

    get_input(field_name) {
        let field_id = this.ID_map.get(field_name);
        for (let i = 0; i < this.form_groups.length; i++)
            if (this.form_groups[i].getAttribute("data-fieldid") == field_id) {
                return this.form_groups[i].getElementsByClassName("form-control")[0].value;
            }
    }

    set_select(field_name, value, text = null) {
        let field_id = this.ID_map.get(field_name);
        for (let i = 0; i < this.form_groups.length; i++)
            if (this.form_groups[i].getAttribute("data-fieldid") == field_id) {
                this.form_groups[i].getElementsByTagName("label")[0].innerHTML =
                    "<b>Modified: " + text ? text : value + "</b>";
                return this.form_groups[i].getElementsByTagName("select")[0].value = value;
            }
    }

    set_select_queue(field_name, value, text = null) {
        this.queue.push([field_name, value, text]);
        window.localStorage.setItem("Queue_select", JSON.stringify(this.queue));
    }

    get_select(field_name) {
        let field_id = this.ID_map.get(field_name);
        for (let i = 0; i < this.form_groups.length; i++)
            if (this.form_groups[i].getAttribute("data-fieldid") == field_id) {
                return this.form_groups[i].getElementsByTagName("select")[0].value;
            }
    }
}

//--------------------------------------------------------------
function save() {
    sn = fields.get_input("Serial Number");
    if (!fields.get_input("Service Tag"))
        fields.set_input("Service Tag", sn);
    if (!fields.get_input("Name"))
        fields.set_input("Name", sn);

    sn_string = fields.get_textarea_element("Comments").value
    regex = /HDD SN:([^\n]*)\n/g
    output = null

    while ((m = regex.exec(sn_string)) !== null) {
        if (m.index === regex.lastIndex) regex.lastIndex++;
        m.forEach((match, groupIndex) => { output = match });
    }

    if (output == null) {
        alert("HDD serial number formatting will not save\nFix if needed");
        return;
    }

    output = output.replace(/^\s+|\s+$/g, '');

    if (!fields.get_input("HDD/SSD Serial Number"))
        fields.set_input("HDD/SSD Serial Number", output);
    console.log(output);
}

var fields;
var per;

window.addEventListener("load", async (event) => {
    fields = new Fields();
    per = new URLSearchParams(window.location.search);
    if (document.getElementById("attribute502")) { // TODO: Make this better
        if (!fields.get_input("Service Tag"))
            fields.set_input("Service Tag", per.get('id'));
        if (!fields.get_input("Serial Number"))
            fields.set_input("Serial Number", per.get('id'));
        if (!fields.get_input("Name"))
            fields.set_input("Name", per.get('id'));
        if (localStorage.getItem("Asset_Id") == per.get('id')) {
            localStorage.removeItem("Substate");
            localStorage.removeItem("Done");
        }
    }

    if (document.getElementById("btnSubmit"))
        document.getElementById("btnSubmit").addEventListener("click", save);

    done = localStorage.getItem("Done");
    if (done) {
        localStorage.removeItem("Done");
        document.body.style.backgroundColor = "lightgreen";
        // for (let i = 200; i > 0; i--) {
        //     document.title = "Closing in " + i + " hours";
        //     await new Promise(r => setTimeout(r, 10));
        // }
        // window.close();
    }
    substate = localStorage.getItem("Substate")
    if (substate) {
        substate = JSON.parse(substate)
        localStorage.removeItem("Substate");
        localStorage.setItem("Done", "true");
        // document.body.style.backgroundColor = "red";
        fields.set_select("Substate", substate[1], substate[0]);
        await new Promise(r => setTimeout(r, 500));
        document.getElementById("btnSubmit").click();
    }
});


document.addEventListener("keydown", (event) => {
    console.log("Edit: " + event.which);

    if (event.which == "112" || event.which == "113") { //F1 & F2
        event.preventDefault();
        let substate = event.which == "112" ? ["Pending repair", 5210] : ["Pending disposal", 5207];
        document.title = substate[0];
        fields.set_input("Owner", "", "Joan Deer");
        fields.set_input("Location", "63", "AHCWARE");
        fields.set_input("Location Room", "", "Out of Room");
        fields.set_select("State", 4524, "In Stock");
        fields.set_select("Substate", substate[1], substate[0]);
        localStorage.setItem("Asset_Id", per.get('id'));
        localStorage.setItem("Substate", JSON.stringify(substate));
    }

    if (event.which == "114" || event.which == "115") { //F3 & F4
        comments = fields.get_textarea_element("Comments");
        event.preventDefault();
        const dat = new Date();
        todays_date = dat.toString();
        comments.value = comments.value ? comments.value + "\n\n" : comments.value;
        if (event.which == "114") {
            comments.value += "----\n" + todays_date + "\nReceived by ReUse.\nHDD SN:N/A\n----";
        } else {
            document.getElementById("attribute2686").value += "----\n" + todays_date + "\nReceived by ReUse.\nHDD SN: ----";
            pos = document.getElementById("attribute2686").value.length - 4;
            document.getElementById("attribute2686").focus();
            document.getElementById("attribute2686").setSelectionRange(pos, pos);
        }
        comments.scrollIntoView(true);
        window.scrollBy(0, -100);
    }



    if (event.which == "27") { //Esc
        event.preventDefault();
        if (document.getElementById("btnEdit")) {
            localStorage.removeItem("Substate");
            localStorage.removeItem("Done");
            document.getElementById("btnEdit").click();
        } if (document.getElementById("btnSubmit")) {
            document.getElementById("btnSubmit").click();
        }
    }


    // if (event.which == "123") { //F12
    //     document.title = "Sold Asset";
    //     event.preventDefault();
    //     if (document.getElementById("btnEdit"))
    //         document.getElementById("btnEdit").click();
    //     fields.set_select("State", 4527, "Retired");
    //     fields.set_select("Substate", 4542, "Sold");

    //     if (document.getElementById("btnSubmit"))
    //         document.getElementById("btnSubmit").click();
    // }
});
