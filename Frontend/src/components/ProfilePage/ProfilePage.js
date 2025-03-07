import React, { useEffect, useState } from 'react';
import Header from "../Header/Header";
import Card from "../UI/Card/Card";
import Button from "../UI/Button/Button";
import './ProfilePage.css';
import {CheckCircleIcon} from "@heroicons/react/outline";

const ProfilePage = () => {
    const [profile, setProfile] = useState(null);
    useEffect(()=>{
        fetch("http://127.0.0.1:8000/api/getUser/aniketkulkarni").then(res=>res.json())
        .then(res=>setProfile(res))
    }, [])
    return (
        <>
            <Header/>
            <div className="profile-page__main">
                <div className="flex w-screen h-screen justify-around items-center">
                    <div className="flex-col">
                        {profile &&
                        <Card className="w-[80vh] pt-6 pb-12 my-10 px-[15%] text-center">


                            <h1 className="profile-page__heading mb-12 mt-5">{profile.first_name + " "+ profile.last_name}</h1>


                            <span className="flex justify-left text-left font-[iceland] certified-lead"><CheckCircleIcon
                                className="my-auto inline h-10 px-4"/> Certified Lead<Button
                                className="self-end ml-auto my-auto">{profile.reward} pts.</Button></span>

                            <hr className="mt-3 w-[25%] border-2 border-black"/>
                            <div className="flex-col gap-[40px] justify-between mt-10">
                                <p className="text-left font-[Montserrat] my-4 font-[400]">Email id</p>
                                <span className="block text-left profile-description p-3">{profile.email}</span>
                                <p className="text-left font-[Montserrat] my-2 font-[400]">Twitter ID</p>
                                <span className="block text-left profile-description p-3">{profile.social_twitter}</span>
                                <p className="text-left font-[Montserrat] my-2 font-[400]">Tags Interested</p>
                                <span className="block text-left profile-description p-3">Finance, Loans</span>

                            </div>


                        </Card>
}

                    </div>

                </div>

            </div>
        </>
);
};

export default ProfilePage;