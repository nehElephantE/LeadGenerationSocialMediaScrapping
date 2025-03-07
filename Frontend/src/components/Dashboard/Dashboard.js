import React, { useEffect, useState } from 'react';
import Header from "../Header/Header";
import Card from "../UI/Card/Card";
import Profile from "../Profile/Profile";
import Banner from "../UI/Banner/Banner";
import {PaperAirplaneIcon, PaperClipIcon} from "@heroicons/react/outline";
import './Dashboard.css';
import {
    PieChart,
    Pie,
    Legend,
    ResponsiveContainer,
    BarChart,
    CartesianGrid,
    XAxis,
    YAxis,
    Tooltip,
    Bar,
    Cell
} from "recharts";

const Dashboard = () => {
    const sentiments = [
        {name: 'Possitive', students: 400, fill: 'green' },
        {name: 'Negative', students: 700, fill: 'red' },
        {name: "Neutral", students: 200, fill: "yellow"}
    ]

    const data = [
        {name: 'Life Insurance', students: 400, fill: '#D61C4E'},
        {name: 'Health Insurance', students: 700, fill: '#F77E21'},
        {name: 'Automobile Insurance', students: 200, fill: '#FAC213'},
        {name: 'Home Insurance', students: 1000, fill: '#A64B2A'}
    ];

    const segregatedData = [
        {
            "name": "Life Insurance",
            "possitive": 4000,
            "negative": 2400
        },
        {
            "name": "Home Insurance",
            "possitive": 3000,
            "negative": 1398
        },
        {
            "name": "Automobile Insurance",
            "possitive": 2000,
            "negative": 9800
        },
        {
            "name": "Health Insurance",
            "possitive": 2780,
            "negative": 3908
        }
      ]
    const [insuranceData, setInsuranceData] = useState([
        {name: 'Possitive', students: 1, fill: 'green' },
        {name: 'Negative', students: 1, fill: 'red' },
        {name: "Neutral", students: 1, fill: "yellow"}
    ]);
    const [chartData, setchartData] = useState(null);
    const [collective, setCollective] = useState([
        {name: 'Life Insurance', students: 0, fill: '#D61C4E' },
        {name: 'Health Insurance', students: 0, fill: '#F77E21' },
        {name: 'Automobile Insurance', students: 0, fill: '#FAC213' },
        {name: 'Home Insurance', students: 0, fill: '#A64B2A' }
    ])
    const [lifeInsurance, setLifeInsurance] = useState(null);
    const [healthInsurance, setHealthInsurance] = useState(null);
    const [homeInsurance, setHomeInsurance] = useState(null);
    const [carInsurance, setCarInsurance] = useState(null);
    const [lifeInsuranceUsers, setLifeInsuranceUsers] = useState(null);
    const [healthInsuranceUsers, setHealthInsuranceUsers] = useState(null);
    const [carInsuranceUsers, setCarInsuranceUsers] = useState(null);
    const [homeInsuranceUsers, setHomeInsuranceUsers] = useState(null);
    const [item, setItem] = useState(0);
    useEffect(()=>{
        fetch("http://127.0.0.1:8000/api/getTwitterSentiments/life-insurance")
        .then(res=>res.json())
        .then(res=>{
            setLifeInsurance(res['data']);
            setLifeInsuranceUsers(res['users']);
            setCollective([
                ...collective,
                collective[0].students = res['data'].length
            ]);
        })
        // .then(life)
        fetch("http://127.0.0.1:8000/api/getTwitterSentiments/health-insurance")
        .then(res=>res.json())
        .then(res=>{
            setHealthInsurance(res['data'])
            setHealthInsuranceUsers(res['users']);
            setCollective([
                ...collective,
                collective[1].students = res['data'].length
            ])
            
    })
    fetch("http://127.0.0.1:8000/api/getTwitterSentiments/insurance")
    .then(res=>res.json())
    .then(res=>{
        setCarInsurance(res['data']);
        setCarInsuranceUsers(res['users']);
        setCollective([
            ...collective,
            collective[2].students = res['data'].length
        ])
        
    })
    fetch("http://127.0.0.1:8000/api/getTwitterSentiments/finance")
    .then(res=>res.json())
    .then(res=>{
            setHomeInsurance(res['data'])
            setHomeInsuranceUsers(res['users']);
            setCollective([
                ...collective,
                collective[3].students = res['data'].length
            ])
    }).then(()=>console.log(collective))

    }, [collective])

    return (
        <div>
            <Header/>
            <div className="home__section overflow-hidden px-10 py-5">
                <span className="dashboard-heading__main px-5">Dashboard</span>
                <div className="flex">
                    <div className="flex flex-col gap-5">
                        <Card className="card py-6 my-5 w-[20rem]">

                            <span className="subheading px-6">
                                Potential Leads
                            </span>
                            <hr/>
                            <div className="h-[68vh] flex-grow overflow-y-scroll">
                                <div className="flex justify-center">
                                    <button className="toggle-button" onClick={()=>setItem(0)}>
                                        <a href="#" title="Header" data-toggle="popover" data-placement="top"
                                           data-content="Content">🧬</a>
                                    </button>
                                    <button className="toggle-button" onClick={()=>setItem(1)}>
                                    <a href="#" title="Header" data-toggle="popover" data-placement="bottom"
                                       data-content="Content">🩺</a>
                                    </button>
                                    <button className="toggle-button" onClick={()=>setItem(2)}>
                                    <a href="#" title="Header" data-toggle="popover" data-placement="left"
                                       data-content="Content">🚗</a>
                                    </button>
                                    <button className="toggle-button" onClick={()=>setItem(3)}>
                                    <a href="#" title="Header" data-toggle="popover" data-placement="right"
                                       data-content="Content">🏚️</a>
                                    </button>
                                </div>
                                {
                                    item ===0 && lifeInsuranceUsers && 
                                    lifeInsuranceUsers.map(data=>(<Profile authorId={"1381371098193747974"} type="square" name={data.name}/>))
                                }
                                {
                                    item ===1 && healthInsuranceUsers && 
                                    healthInsuranceUsers.map(data=>(<Profile type="square" name={data.name}/>))
                                }
                                {
                                    item ===2 && carInsuranceUsers && 
                                    carInsuranceUsers.map(data=>(<Profile type="square" name={data.name}/>))
                                }
                                {
                                    item ===3 && homeInsuranceUsers && 
                                    homeInsuranceUsers.map(data=>(<Profile type="square" name={data.name}/>))
                                }
                            </div>
                        </Card>
                    </div>
                    <div className="block flex flex-grow px-5 justify-evenly my-5 ">

                        <div>
                            <span
                                className="block dashboard-heading__chart px-5 text-center">Insurance Sentiments</span>
                            <ResponsiveContainer width={700} height="80%">
                                <PieChart width={500} height={500}>
                                    <Legend verticalAlign="bottom" align="center"/>
                                    <Pie data={sentiments} dataKey="students" outerRadius={250}/>
                                </PieChart>
                            </ResponsiveContainer>
                        </div>
                        <div>
                            <span
                                className="block dashboard-heading__chart px-5 text-center">Insurance Distributions</span>
                            <ResponsiveContainer width={700} height="80%">
                                <PieChart width={500} height={500}>
                                    <Legend verticalAlign="bottom" align="center"/>
                                    <Pie data={collective} dataKey="students" outerRadius={250} fill="green"/>
                                </PieChart>
                            </ResponsiveContainer>
                        </div>

                    </div>
                </div>


            </div>
            <div className="flex flex-grow px-5 justify-evenly bg-[#B9E5FF]">

                <div>
                    <span className="block dashboard-heading__chart px-5 text-center">Segregagted Sentiments</span>
                    <BarChart width={1200} height={500} data={segregatedData}>
                        <CartesianGrid strokeDasharray="3 3"/>
                        <XAxis dataKey="name"/>
                        <YAxis/>
                        <Tooltip/>
                        <Legend/>
                        <Bar dataKey="negative" fill="#F15412"/>
                        <Bar dataKey="possitive" fill="#A0D995"/>
                    </BarChart>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;