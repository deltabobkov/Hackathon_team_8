import Avatar from '@mui/material/Avatar';
import { Link, useLocation } from 'react-router-dom';
import './VacancyCard.scss';
import { Checkbox } from '@mui/material';
import { useDispatch } from 'react-redux';
import { useState, useRef } from 'react';
import { ICandidate } from '../../store/foundCandidates/foundCandidates';
// import checkboxChecked from '../../assets/icons/checkboxChecked.svg';
// import checkbox from '../../assets/icons/checkbox.svg';
import like from '../../assets/icons/Like.svg';
import likeFilled from '../../assets/icons/Like filled.svg';
import { addCandidateInfo } from '../../store/candidateInfo/candidateInfo';

interface VacancyCardProps {
  card: ICandidate;
  liked: boolean;
}

function VacancyCard({ card, liked = false }: VacancyCardProps) {
  const [checked, setChecked] = useState(liked);
  const cardRef = useRef(null);
  const dispatch = useDispatch();
  const handlerCardClick = () => {
    dispatch(addCandidateInfo(card));
    // navigate(`/candidates/${card.id}`);
  };

  const location = useLocation();

  function createLink(to: string) {
    return {
      pathname: to,
      state: { from: location.pathname },
    };
  }

  return (
    <article className={`card ${checked ? 'card_checked' : ''}`}>
      <Link to={createLink(`/candidates/${card.id}`)} onClick={handlerCardClick}>
        {/* <Checkbox
        disableRipple
        sx={{
          padding: 0, paddingTop: '17px', height: 'fit-content', width: 20,
        }}
        icon={<img alt="checkbox-field" src={checkbox} />}
        checkedIcon={<img alt="checkbox-field" src={checkboxChecked} />}
      /> */}
        <div ref={cardRef} className="card__info">
          <Avatar
            className="card__avatar"
            alt="Аватар пользователя"
            src={card.image}
            sx={{
              width: 53, height: 53, marginRight: '11px', marginLeft: 0,
            }}
            aria-label="recipe"
          />
          <div className="card__description">
            <div className="card__candidate-info">
              <p className="card__candidate-name">{`${card?.first_name} ${card?.last_name}`}</p>
              <p className="card__city">{card?.location}</p>
            </div>
            <h2 className="card__profession">{card?.location.split(', ')}</h2>
            <div className="card__experience">
              <p className="card__level">{card?.level}</p>
              <p className="card__attempt">
                Опыт работы:
                {' '}
                <span className="card__period">
                  {card.experience}
                </span>
              </p>
            </div>
          </div>
        </div>
      </Link>
      <div className="card__favorite">
        <Checkbox
          className="card__checkbox"
          disableRipple
          sx={{
            padding: '6px',
            backgroundColor: 'var(--Blue-BG)',
            height: 'fit-content',
            width: '32px',
            borderRadius: '6px',
          }}
          icon={<img alt="checkbox-field" src={like} />}
          checkedIcon={<img alt="checkbox-field" src={likeFilled} />}
          checked={checked}
          onChange={(e) => {
            setChecked(e.target.checked);
          }}
        />
        {/* <p className="card__status">
          Статус:
          {' '}
          <span className="card__vacancy">
            вакансия отправлена
          </span>
        </p> */}
      </div>
    </article>
  );
}

export default VacancyCard;
