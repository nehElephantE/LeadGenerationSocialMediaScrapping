import React, { useState, useEffect } from "react";
import "./Leaderboard.css";

const Leaderboard = () => {
  const [leaderboard, setLeaderBoard] = useState(null);
  useEffect(()=>{
    fetch("http://127.0.0.1:8000/api/getLeaderboard")
    .then(res=>res.json())
    .then(res=>setLeaderBoard(res.data))
  }, [])
  return (
    <div class="leaderboard">
      <h1>
        <svg class="ico-cup">
          <use href="#cup"></use>
        </svg>
        Most active Players
      </h1>
      <ol>
        {leaderboard && leaderboard.map(val=>(
        <li>
          <mark>{val.first_name+ " "+val.last_name}</mark>
          <small>{val.reward}</small>
        </li>
        ))}
      </ol>
    </div>
  );
};

export default Leaderboard;
