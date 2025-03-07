import React from 'react';
import './CommCard.css';


const CommCard = (props) => {
    return (
        // <div className={`${props.className}`}>
            <div className="max-w-sm relative container-main w-[100%] h-[100%] rounded-[12px] my-5">
                <div
                    className="bg-no-repeat absolute inset-x-0 bottom-0 frost w-[100%] h-[65%] flex justify-center">
                    <div className="flex-col w-[100%]">
                        <div className="text-center">
                            image
                        </div>
                        <div className="text-right ml-3">
                            <span className="block commcard-heading text-left">Gaming Circle</span>
                        </div>
                        <div className="commcard-desc  ml-3">A circle for gamers to explore all stuff ranging from
                            mechanical keyboards to monitors.
                        </div>
                        <div className="ml-3 text">
                            <p className="inline-block commcard-online">5678 Online</p>

                        </div>


                    </div>

                </div>
            </div>
        // </div>
    );
};

export default CommCard;