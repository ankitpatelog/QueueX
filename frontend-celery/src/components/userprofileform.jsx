import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import axios from 'axios';

export default function Register() {

  const [form, setForm] = useState({
    email: "",
    password: "",
    first_name: "",
    last_name: "",
  });

  const [eyeopen, setEyeOpen] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault(); 
    console.log(form);

    try {
      const response = axios.post('http://127.0.0.1:8000/api/register/', form);
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center px-6 bg-[#0A0A0F] relative overflow-hidden">

      {/* Glow */}
      <div className="absolute w-[500px] h-[500px] bg-purple-700 opacity-20 blur-3xl rounded-full top-[-100px] left-[-100px]"></div>
      <div className="absolute w-[400px] h-[400px] bg-cyan-500 opacity-20 blur-3xl rounded-full bottom-[-100px] right-[-100px]"></div>

      <div className="w-full max-w-md relative z-10">

        {/* Heading */}
        <div className="text-center mb-10">
          <h1 className="text-3xl font-semibold text-white tracking-tight">
            Create an account
          </h1>
          <p className="text-gray-400 text-sm mt-2">
            Enter your details to create an account on QueueX
          </p>
        </div>

        {/* Form */}
        <form 
          onSubmit={handleSubmit}
          className="backdrop-blur-xl bg-white/5 border border-white/10 rounded-2xl p-8 space-y-5 shadow-[0_0_40px_rgba(0,0,0,0.5)]"
        >

          {/* Email */}
          <input
            type="email"
            placeholder="Email"
            value={form.email}
            onChange={(e) => setForm({ ...form, email: e.target.value })}
            className="w-full px-4 py-2.5 rounded-lg bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:ring-1 focus:ring-cyan-400 outline-none"
          />

          {/* First Name */}
          <input
            type="text"
            placeholder="First Name"
            value={form.first_name}
            onChange={(e) => setForm({ ...form, first_name: e.target.value })}
            className="w-full px-4 py-2.5 rounded-lg bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:ring-1 focus:ring-purple-400 outline-none"
          />

          {/* Last Name */}
          <input
            type="text"
            placeholder="Last Name"
            value={form.last_name}
            onChange={(e) => setForm({ ...form, last_name: e.target.value })}
            className="w-full px-4 py-2.5 rounded-lg bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:ring-1 focus:ring-purple-400 outline-none"
          />

          {/* Password */}
          <div className="relative">
            <input
              type={eyeopen ? "text" : "password"}  // ✅ FIXED
              placeholder="Password"
              value={form.password}
              onChange={(e) => setForm({ ...form, password: e.target.value })}
              className="w-full px-4 py-2.5 pr-10 rounded-lg bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:ring-1 focus:ring-pink-400 outline-none"
            />

            {/* Toggle Icon */}
            <div
              onClick={() => setEyeOpen(!eyeopen)}
              className="absolute right-3 top-1/2 -translate-y-1/2 cursor-pointer text-gray-400 hover:text-white"
            >
              {eyeopen ? <FaEyeSlash /> : <FaEye />}
            </div>
          </div>

          {/* Button */}
          <button
            type="submit"
            className="w-full py-2.5 rounded-lg font-medium text-white 
            bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 
            hover:opacity-90 transition shadow-lg shadow-purple-500/20"
          >
            Create Account
          </button>

        </form>

        {/* Footer */}
        <p className="text-center text-sm text-gray-500 mt-6">
          Already have an account?{" "}
          <span className="text-cyan-400 cursor-pointer hover:underline">
            Sign in
          </span>
        </p>

      </div>
    </div>
  );
}