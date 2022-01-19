let food = document.getElementById('table1');
let disease = document.getElementById('table2');
let vaccine = document.getElementById('table3');
let youtubeExist = document.getElementById('youtube_exist');
const foodTable = document.querySelector('#food_table');
const diseaseTable = document.querySelector('#disease_table');
const vaccineTable = document.querySelector('#vaccine_table');
const youtubeBlock = document.querySelector('#youtube_exist');
const playerBlock = document.querySelector('#player_status');
let foodTableStatus = foodTable.style.display;
let diseaseTableStatus = diseaseTable.style.display;
let vaccineTableStatus = vaccineTable.style.display;
let youtubeExistStatus = youtubeExist.innerHTML;
let playerBlockStatus = playerBlock.style.display;


food.onclick = function() {
    if(foodTableStatus == 'table') {
        foodTable.style.display = 'none';
        foodTableStatus = foodTable.style.display = 'none';
    } else if(foodTableStatus == 'none') {
        foodTable.style.display = 'table';
        foodTableStatus = foodTable.style.display = 'table';
    }
}

disease.onclick = function() {
    if(diseaseTableStatus == 'table') {
        diseaseTable.style.display = 'none';
        diseaseTableStatus = diseaseTable.style.display = 'none';
    } else if(diseaseTableStatus == 'none') {
        diseaseTable.style.display = 'table';
        diseaseTableStatus = diseaseTable.style.display = 'table';
    }
}

vaccine.onclick = function() {
    if(vaccineTableStatus == 'table') {
        vaccineTable.style.display = 'none';
        vaccineTableStatus = vaccineTable.style.display = 'none';
    } else if(vaccineTableStatus == 'none') {
        vaccineTable.style.display = 'table';
        vaccineTableStatus = vaccineTable.style.display = 'table';
    }
}

youtubeExist.onclick = function() {
    if (youtubeExistStatus == '[영상 열기]') {
        youtubeBlock.innerHTML = '[영상 닫기]';
        youtubeExistStatus = youtubeExist.innerHTML = '[영상 닫기]';
        playerBlock.style.display = 'block';
    } else if (youtubeExistStatus == '[영상 닫기]') {
        youtubeBlock.innerHTML = '[영상 열기]';
        youtubeExistStatus = youtubeExist.innerHTML = '[영상 열기]';
        playerBlock.style.display = 'none';
    }
}


