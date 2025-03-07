import React from 'react';

import './Profile.css';
import {useDispatch} from "react-redux";
import {useNavigate} from "react-router-dom";
import {setChannelInfo} from "../../features/channelSlice";

const Profile = ({id, name, authorId}) => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const setChannel = () => {
        dispatch(setChannelInfo({
            channelId: id,
            channelName: name,
        }))
        navigate(`/channels/${id}`)
    };
    function handleOnclick(){
        fetch("http://127.0.0.1:8000/api/sendTweet/"+authorId).then(res=>res.json())
    }
    return (
        <div
            className='profile__container flex align-middle px-6 py-3 scrollbar-hide min-h-[1rem] cursor-pointer overflow-hidden transition-all ease-out duration-200'
            onClick={setChannel}
        >
            <button className='flex' onClick={handleOnclick}>

            {/*<img className={`${type} h-10 w-10 profile__img`}*/}
            {/*     src="https://thumbs.dreamstime.com/b/rainbow-love-heart-background-red-wood-60045149.jpg" alt=""/>*/}


            <div className="main">
                <div className="flex flex-row">
                    <div className="d1">🧬</div>
                    <div className="d1">🩺</div>
                </div>
                <div className="flex flex-row">
                    <div className="d1">🚗</div>
                    <div className="d1">🏚️</div>
                </div>
            </div>

            <span className='profile-name px-4 align-middle place-self-center'>{name}</span>
            </button>
        </div>
    );
};

export default Profile;