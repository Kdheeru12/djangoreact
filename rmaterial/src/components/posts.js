import React,{useState,useEffect} from 'react';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import Link from '@material-ui/core/Link';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import axios from 'axios'
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
  root: {
    maxWidth: 345,
  },
  media: {
    height: 140,
  }
}));

export default function SignIn() {
  const classes = useStyles();
  const [posts, setposts] = useState([]);  
  const [loading, setloading] = useState(true);
  useEffect(() => {
      axios.get('http://127.0.0.1:8000/')
      .then(res => {
          setposts(res.data)
          setloading(false)
      })
  }, []);

  return (
    <div>
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Typography component="h1" variant="h5">
        {loading && 'Posts loading'}
        </Typography>
        </div>
    {posts.map(i =>(
    <div key={i.id}>
    <Card  className={classes.root}>
    <CardActionArea>
        <CardContent>
        <Typography gutterBottom variant="h5" component="h2">
            {i.title}
        </Typography>
        <Typography variant="body2" color="textSecondary" component="p">
           {i.content}
        </Typography>
        </CardContent>
    </CardActionArea>
    <CardActions>
        <Button size="small" color="primary">
        Share
        </Button>
        <Button href={`/${i.id}`} size="small" color="primary">
        Learn More
        </Button>
    </CardActions>
    </Card>
    </div>
    ))}
      <Box mt={8}>
        <Copyright />
      </Box>
    </Container>
    
    </div>    
  );
}