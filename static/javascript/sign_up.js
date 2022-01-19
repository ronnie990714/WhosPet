let kind1 = document.getElementById('common')
let kind2 = document.getElementById('vet')
let kind3 = document.getElementById('company')
const commonNum = document.querySelector('#id_user_pet_num').parentElement;
const vetNum = document.querySelector('#id_user_vet_num').parentElement;
const companyName = document.querySelector('#id_user_comp_name').parentElement;
const companyAddress = document.querySelector('#id_user_comp_address').parentElement;
const common = document.querySelector('#common');
const vet = document.querySelector('#vet');
const company = document.querySelector('#company');

// 처음은 일반사용자 가입만 나오게
vetNum.style.display = 'none';
companyName.style.display = 'none';
companyAddress.style.display = 'none';

kind1.onclick = function() {
    commonNum.style.display = 'flex';
    vetNum.style.display = 'none';
    companyName.style.display = 'none';
    companyAddress.style.display = 'none';
    common.style.border = '2px solid red';
    vet.style.border = '2px solid black';
    company.style.border = '2px solid black';
}

kind2.onclick = function() {
    commonNum.style.display = 'none';
    vetNum.style.display = 'flex';
    companyName.style.display = 'none';
    companyAddress.style.display = 'none';
    common.style.border = '2px solid black';
    vet.style.border = '2px solid red';
    company.style.border = '2px solid black';
}

kind3.onclick = function() {
    commonNum.style.display = 'none';
    vetNum.style.display = 'none';
    companyName.style.display = 'flex';
    companyAddress.style.display = 'flex';
    common.style.border = '2px solid black';
    vet.style.border = '2px solid black';
    company.style.border = '2px solid red';
}

