import { Button, DialogActions, Divider, Typography,Select,MenuItem, Input } from "@mui/material";
import './gitpushmodal.css'
import { useState, useEffect } from 'react';



export default function GitPushModal(props){

    const [rep,setRep] = useState('');
    const [com,setCom] = useState('');
    const [branch,setBranch] = useState('');
    const [branchList,setBranchList] = useState([]);
    const [repinfo,setRepinfo] = useState(null)
    const handleRepChange = (event) => {
        const selectedRepositoryName = event.target.value;
        const selectedRepository = props.gitreplist.find((item) => item.repository_name === selectedRepositoryName);
        setRepinfo(selectedRepository);
        setRep(selectedRepositoryName);
    };
    useEffect(()=>{
        getBranchList()
    },[repinfo])
    const handleComChange = (event) => {
        setCom(event.target.value);
    };
    const handleBranchChange = (event) => {
        setBranch(event.target.value);
    };
    
    const getBranchList = async (id) => {
        const jwtToken = sessionStorage.getItem("jwt");
        try {
          const response = await fetch(`http://127.0.0.1:8000/get-branch/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${jwtToken}`,
            },
            body: JSON.stringify({
                'url' : repinfo.repository_url,
                'name': repinfo.repository_name,
            })
          })
          const data = await response.json();
          console.log(data)
          setBranchList(data['branches'])
        } catch (error) {
          console.log(error)
        }
    }
    return(
        <div className="modal-box h-full">
            <div className="title-text mb-4 mt-4">
            <Typography className="title-text">Push code to GitHub</Typography>
            </div>
            <Divider className="divider"></Divider>
            <div className="input-box mt-4 mb-4 flex">
                <Button className="input-box-text" onClick={props.handleOpenSelectFiles}>
                Select files to push to GitHub
                </Button>
                <div className="flex flex-col h-10 overflow-y-scroll">
                {
                    props.selectedfilelist?.map((item)=>(
                        <Typography>{item.filename}</Typography>
                    ))
                }
                </div>
                
            </div>
            <Divider className="divider"></Divider>
            <div className="input-box mt-4 mb-4">
                <Typography className="input-box-text">
                Select Target Repository
                </Typography>
                <Select className='select' value={rep} onChange={handleRepChange}>
                    {
                        props.gitreplist?.map((item, index) => (
                            <MenuItem value={item.repository_name}>{item.repository_name}</MenuItem>
                          ))
                    }
                    <MenuItem value={3} onClick={props.handleOpenRepModal}>Create New Repository</MenuItem>
                </Select>
            </div>
            <Divider className="divider"></Divider>
            <div className="input-box mt-4 mb-4">
                <Typography className="input-box-text">
                Select Target Branch
                </Typography>
                <Select className='select' value={branch} onChange={handleBranchChange}>
                    {
                        branchList?.map((item, index) => (
                            <MenuItem value={item}>{item}</MenuItem>
                          ))
                    }
                    <MenuItem value={30} onClick={props.handleOpenBranchModal}>Create New Branch</MenuItem>
                </Select>
            </div>
            <Divider className="divider"></Divider>
            <div className="input-box mt-4 mb-4">
                <Typography className="input-box-text">
                Enter Commit Message
                </Typography>
                <Input value={com} onChange={handleComChange}></Input>
            </div>
            <Divider className="divider"></Divider> 
            <DialogActions className="buttons">
                <Button className="cancel" onClick={props.handleCloseModal}>
                    Cancel
                </Button>
                <Button variant="contained" className="push">
                    Push
                </Button>
            </DialogActions>
        </div>
    )
}