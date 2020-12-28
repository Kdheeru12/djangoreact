import React ,{useState}from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { useHistory } from 'react-router';
import {AxiosSend} from './Axios'

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

//login component

function Login() {
  const classes = useStyles();
  const history = useHistory()
  const initialState = Object.freeze({
    username:'',
    password:'',
  })
  const errorState = {
    error: '',
    }
  const [data, setdata] = useState(initialState)
  const [error, seterror] = useState(errorState)
  const Change = (e) =>{
    setdata({
      ...data,
      [e.target.name] : e.target.value.trim(),
    })
    
  }

  const Submit = (e) =>{
    e.preventDefault();
    console.log(data);
    AxiosSend
      .post(`token/`,{
      username:data.username,
      password:data.password,
    })
    .then((res) =>{
      localStorage.setItem('access_token',res.data.access);
      localStorage.setItem('refresh_token',res.data.refresh);
      AxiosSend.defaults.headers['Authorization'] = 
      'JWT ' + localStorage.getItem('access_token');

      console.log(AxiosSend.defaults.headers)
    })
    .catch(error =>{
      if (typeof error.response === 'undefined') {
        
        return Promise.reject(error);
      }
      else if (error.response.data.detail === 'No active account found with the given credentials')
      {
        seterror({
          error:'Invalid username or password'
        })
      }
    })
  }
  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <form onSubmit={Submit} className={classes.form} noValidate>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="username"
            label="username"
            name="username"
            autoComplete="username"
            onChange={Change}
            autoFocus
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={Change}
          />
          {error.error}
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Sign In
          </Button>
          <Grid container>
            <Grid item xs>
              <Link href="#" variant="body2">
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link href="#" variant="body2">
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={8}>
        <Copyright />
      </Box>
    </Container>
  );
}

export default Login